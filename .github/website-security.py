from collections import Counter
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

WEBSITE_REPOSITORY = 'makerspace-partheland/makerspace-partheland.github.io'
GITHUB_SERVER = 'https://github.com'
GITHUB_API = 'https://api.github.com'
CISA_CATALOG = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'

STABLE_VERSION = re.compile(r'v?(\d+\.\d+\.\d+)')
ACTION_SOURCE = re.compile(r'([A-Za-z0-9-]+/[A-Za-z0-9_.-]+)(?:/[A-Za-z0-9_./-]+)?@([A-Za-z0-9_./-]+)')
ADVISORY_ID = re.compile(r'GHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}')
CVE_ID = re.compile(r'CVE-\d{4}-\d{4,}')
SEVERITY = {
    'critical': 'Kritisch',
    'high': 'Hoch',
    'medium': 'Mittel',
    'moderate': 'Mittel',
    'low': 'Niedrig',
    'unknown': 'Unbekannt',
}


def github_items(endpoint):
    # Die Ausgabe bleibt auch bei aktiver Runner-Diagnose im Prozess.
    result = subprocess.run(
        ['gh', 'api', '--hostname', 'github.com', '--paginate', '--slurp',
         '-H', 'Accept: application/vnd.github+json', '-H', 'X-GitHub-Api-Version: 2026-03-10',
         endpoint],
        env={'PATH': os.environ['PATH'], 'GH_TOKEN': os.environ['GH_TOKEN'], 'GH_PROMPT_DISABLED': '1'},
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=True,
        timeout=100,
    )
    pages = json.loads(result.stdout)
    if not isinstance(pages, list) or not pages or any(not isinstance(page, list) for page in pages):
        raise ValueError('GitHub-Listenformat')
    return (record for page in pages for record in page)


def check_dependabot():
    if os.environ['GH_SERVER_URL'] != GITHUB_SERVER or os.environ['GITHUB_REPOSITORY'] != WEBSITE_REPOSITORY:
        raise ValueError('Repository-Kontext')

    alerts_path = f'repos/{WEBSITE_REPOSITORY}/dependabot/alerts'
    for alert in github_items(f'{alerts_path}?state=open&per_page=100'):
        number = alert['number']
        if (type(number) is not int or number < 1 or alert['state'] != 'open'
                or alert['url'] != f'{GITHUB_API}/{alerts_path}/{number}'):
            raise ValueError('Alert-Zuordnung')

        package = alert['dependency']['package']
        vulnerability = alert['security_vulnerability']
        advisory = alert['security_advisory']
        if any(not isinstance(package[field], str) or not package[field].strip()
               or package[field] != vulnerability['package'][field] for field in ('ecosystem', 'name')):
            raise ValueError('Alert-Paket')
        if advisory['severity'] not in SEVERITY or vulnerability['severity'] not in SEVERITY:
            raise ValueError('Alert-Schweregrad')
        fixed = vulnerability['first_patched_version']
        if fixed is not None and (not isinstance(fixed['identifier'], str) or not fixed['identifier'].strip()):
            raise ValueError('Alert-Patchversion')

    # Alle gültigen Antworten enden identisch. Meldungsdetails stehen im Security-Bereich.


def workflow_actions():
    # Die Website-Workflows verwenden Block-YAML. Alle lokalen Workflowdateien werden gelesen.
    actions = {}
    for workflow in sorted(Path('.github/workflows').glob('*.y*ml')):
        for line in workflow.read_text(encoding='utf-8').splitlines():
            key, colon, value = line.lstrip(' -').partition(':')
            if not colon or key.strip() != 'uses':
                continue
            source = value.split('#', 1)[0].strip().strip("'\"")
            if source.startswith('./'):
                continue
            match = ACTION_SOURCE.fullmatch(source)
            if not match:
                raise ValueError('Action-Referenzformat')
            repository, reference = match.groups()
            actions.setdefault(repository, set()).add(reference)
    if not actions:
        raise ValueError('Action-Referenzen fehlen')
    return actions


def action_versions(repository, references):
    versions = {reference: set() for reference in references}
    for tag in github_items(f'repos/{repository}/tags?per_page=100'):
        match = STABLE_VERSION.fullmatch(tag['name'])
        if not match:
            continue
        sha = tag['commit']['sha']
        for reference in references.intersection((sha, tag['name'])):
            versions[reference].add(match[1])
    return versions


def published_advisories(repository, versions):
    affected = [f'{repository}@{version}' for version in sorted(versions)] if versions else [repository]
    advisories = {}
    for advisory_type in ('reviewed', 'malware'):
        query = urlencode({
            'ecosystem': 'actions', 'affects': ','.join(affected), 'type': advisory_type,
            'is_withdrawn': 'false', 'per_page': 100,
        })
        for advisory in github_items(f'advisories?{query}'):
            identifier = advisory['ghsa_id']
            if not ADVISORY_ID.fullmatch(identifier):
                raise ValueError('Advisory-Kennung')
            cve = advisory['cve_id']
            if cve is not None and not CVE_ID.fullmatch(cve):
                raise ValueError('CVE-Kennung')
            advisories[identifier] = (SEVERITY[advisory['severity']], cve)
    return advisories


def public_catalog_report():
    request = Request(CISA_CATALOG, headers={'User-Agent': 'makerspace-website-security'})
    with urlopen(request, timeout=30) as response:
        exploited_cves = {record['cveID'] for record in json.load(response)['vulnerabilities']}
    if not exploited_cves or any(not CVE_ID.fullmatch(cve) for cve in exploited_cves):
        raise ValueError('CISA-Katalogformat')

    version_matches = {}
    package_notices = {}
    unresolved = 0
    for repository, references in workflow_actions().items():
        versions_by_reference = action_versions(repository, references)
        for versions in versions_by_reference.values():
            if len(versions) == 1:
                version_matches.update(published_advisories(repository, versions))
            else:
                unresolved += 1
        if any(len(versions) != 1 for versions in versions_by_reference.values()):
            package_notices.update(published_advisories(repository, set()))

    by_severity = Counter(severity for severity, cve in version_matches.values())
    matched_kev = {cve for severity, cve in version_matches.values() if cve in exploited_cves}
    report = [
        '## Öffentliche Sicherheitshinweise für GitHub Actions',
        '',
        '### Hinweise nach aktuellem Versionsstand der GitHub-Tags',
        '',
        'Gezählt werden Hinweise, deren Versionsangabe zum heutigen Tag-Ziel passt. Frühere Tag-Ziele sind daraus nicht ersichtlich.',
        '',
        *(f'- {severity} ({by_severity[severity]})' for severity in dict.fromkeys(SEVERITY.values())),
        f'- Zugehörige CVE im CISA-KEV-Katalog ({len(matched_kev)})',
        '',
        '### Offene Versionszuordnung',
        '',
        f'- Action-Referenzen ohne stabile Versionszuordnung ({unresolved})',
        f'- Öffentliche Pakethinweise mit ungeklärter Anwendbarkeit ({len(package_notices)})',
        '',
    ]
    Path(os.environ['GITHUB_STEP_SUMMARY']).write_text('\n'.join(report), encoding='utf-8')


def main(mode):
    try:
        if mode == 'alerts':
            check_dependabot()
        elif mode == 'actions':
            public_catalog_report()
        else:
            raise ValueError('Prüfmodus')
    except Exception:
        # Keine Exceptions oder API-Inhalte an den Runner weitergeben.
        print('Die Sicherheitsprüfung konnte technisch nicht abgeschlossen werden.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) == 2 else ''))
