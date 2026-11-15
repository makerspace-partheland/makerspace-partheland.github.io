"""Bindet geprüfte Pages-Artefakte an GitHub-Lauf, Quellbaum und ZIP-Digest."""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import zipfile

REPO = os.environ['GITHUB_REPOSITORY']


def api(path):
    return json.loads(subprocess.check_output(['gh', 'api', f'repos/{REPO}/' + path], text=True))


def archive(metadata, destination=None):
    if metadata['expired']:
        raise FileNotFoundError('Pages-Artefakt ist abgelaufen')
    target = Path(os.environ['RUNNER_TEMP']) / ('pages-' + str(metadata['id']) + '.zip')
    try:
        with target.open('wb') as stream:
            subprocess.run(['gh', 'api', f'repos/{REPO}/actions/artifacts/{metadata["id"]}/zip'], stdout=stream, check=True)
        with target.open('rb') as stream:
            if 'sha256:' + hashlib.file_digest(stream, 'sha256').hexdigest() != metadata['digest']:
                raise ValueError('Pages-ZIP stimmt nicht mit GitHub überein')
        with zipfile.ZipFile(target) as bundle:
            expected = {'artifact.tar'} if destination else {'pages-source.json'}
            if set(bundle.namelist()) != expected:
                raise ValueError('Unerwarteter Pages-Archivinhalt')
            if destination:
                with bundle.open('artifact.tar') as source, Path(destination).open('wb') as output:
                    import shutil
                    shutil.copyfileobj(source, output)
            else:
                return json.loads(bundle.read('pages-source.json'))
    finally:
        target.unlink(missing_ok=True)


def validated(run_id, tree):
    if not re.fullmatch('[1-9][0-9]*', run_id):
        raise ValueError('Ungültige Pages-Laufkennung')
    for _ in range(20):
        run = api('actions/runs/' + run_id)
        if run['status'] == 'completed':
            break
        time.sleep(3)
    if (run['repository']['full_name'] != REPO or run['path'] != '.github/workflows/pages.yml'
            or run['event'] != 'pull_request' or run['conclusion'] != 'success'):
        raise ValueError('Der Pages-Prüflauf ist nicht erfolgreich oder stammt aus einem anderen Ablauf')
    artifacts = api('actions/runs/' + run_id + '/artifacts?per_page=100')['artifacts']
    matches = [a for a in artifacts if a['name'] == f'pages-source-{run_id}-{run["run_attempt"]}' and not a['expired']]
    if len(matches) != 1:
        raise FileNotFoundError('Gebundener Pages-Nachweis fehlt')
    proof = archive(matches[0])
    if (proof['repository'] != REPO or proof['run_id'] != int(run_id)
            or proof['attempt'] != run['run_attempt'] or proof['source_sha'] != run['head_sha']
            or proof['source_tree'] != tree
            or api('commits/' + proof['source_sha'])['commit']['tree']['sha'] != tree):
        raise ValueError('Der Pages-Nachweis gehört zu einem anderen Quellbaum')
    page = api('actions/artifacts/' + str(proof['artifact_id']))
    if page['expired']:
        raise FileNotFoundError('Pages-Artefakt ist abgelaufen')
    if page['workflow_run']['id'] != int(run_id) or page['digest'] != proof['artifact_digest']:
        raise ValueError('Das Pages-Artefakt gehört nicht zum Nachweis')
    test_run = proof.get('test_run', int(run_id))
    test = api('actions/runs/' + str(test_run))
    if (test['conclusion'] != 'success' or test['path'] != '.github/workflows/pages.yml'
            or test['repository']['full_name'] != REPO
            or api('commits/' + test['head_sha'])['commit']['tree']['sha'] != tree):
        raise ValueError('Die ursprüngliche Funktionsprüfung gehört zu einem anderen Stand')
    jobs = api(f'actions/runs/{test_run}/attempts/{test["run_attempt"]}/jobs?per_page=100')['jobs']
    if not any(j['conclusion'] == 'success' and 'self-hosted' not in j['labels'] and
               any(s['name'] == 'Menü und Galerie testen' and s['conclusion'] == 'success' for s in j['steps']) for j in jobs):
        raise ValueError('Die ursprüngliche Browserprüfung wurde nicht erfolgreich ausgeführt')
    return proof, page


def record(artifact_id, test_run=None):
    metadata = api('actions/artifacts/' + artifact_id)
    run = int(os.environ['GITHUB_RUN_ID'])
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    if metadata['workflow_run']['id'] != run or metadata['expired']:
        raise ValueError('Das Pages-Artefakt gehört nicht zu diesem Lauf')
    workflow_sha = os.environ['PAGES_WORKFLOW_SHA']
    tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip()
    if api('commits/' + workflow_sha)['commit']['tree']['sha'] != tree:
        raise ValueError('Der ausgeführte Workflow enthält ungeprüfte Basisänderungen')
    data = {'repository': REPO, 'run_id': run, 'attempt': int(os.environ['GITHUB_RUN_ATTEMPT']),
            'source_sha': source, 'source_tree': tree, 'workflow_sha': workflow_sha,
            'artifact_id': int(artifact_id), 'artifact_digest': metadata['digest'], 'test_run': int(test_run or run)}
    (Path(os.environ['RUNNER_TEMP']) / 'pages-source.json').write_text(json.dumps(data) + '\n')


def resolve(requested):
    tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip()
    if requested:
        candidates = [requested]
    else:
        candidates = [str(r['id']) for r in api('actions/workflows/pages.yml/runs?event=pull_request&status=success&per_page=20')['workflow_runs']
                      if r['id'] != int(os.environ['GITHUB_RUN_ID']) and api('commits/' + r['head_sha'])['commit']['tree']['sha'] == tree]
    for run in candidates:
        try:
            proof, metadata = validated(run, tree)
        except FileNotFoundError:
            continue
        (Path(os.environ['RUNNER_TEMP']) / 'pages-reuse.json').write_text(json.dumps({'proof': proof, 'artifact': metadata}))
        with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
            stream.write('reuse=true\n')
        return
    with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
        stream.write('reuse=false\n')


if __name__ == '__main__':
    phase = sys.argv[1]
    if phase == 'record':
        record(*sys.argv[2:])
    elif phase == 'resolve':
        resolve(sys.argv[2] if len(sys.argv) > 2 else '')
    elif phase == 'download':
        data = json.loads((Path(os.environ['RUNNER_TEMP']) / 'pages-reuse.json').read_text())
        archive(data['artifact'], Path(os.environ['RUNNER_TEMP']) / 'artifact.tar')
        with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
            stream.write('test_run=' + str(data['proof']['test_run']) + '\n')
