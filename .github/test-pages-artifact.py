"""Schützt die Wiederverwendung gegen beschädigte Archive und fremde Quellstände."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

os.environ.setdefault('GITHUB_REPOSITORY', 'makerspace-partheland/makerspace-partheland.github.io')
spec = importlib.util.spec_from_file_location('pages', Path(__file__).with_name('pages-artifact.py'))
pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages)


class ArtifactTests(unittest.TestCase):
    def test_download_preserves_tar_and_checks_github_digest(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, 'w') as bundle:
            bundle.writestr('artifact.tar', b'tested static files')
        content = memory.getvalue()
        metadata = {'id': 7, 'expired': False, 'digest': 'sha256:' + hashlib.sha256(content).hexdigest()}
        def transfer(*args, **kwargs):
            kwargs['stdout'].write(content)
            return subprocess.CompletedProcess([], 0)
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {'RUNNER_TEMP': directory}), \
                patch.object(pages.subprocess, 'run', side_effect=transfer):
            destination = Path(directory, 'artifact.tar')
            pages.archive(metadata, destination)
            self.assertEqual(destination.read_bytes(), b'tested static files')
            metadata['digest'] = 'sha256:' + '0' * 64
            with self.assertRaisesRegex(ValueError, 'ZIP stimmt nicht'):
                pages.archive(metadata, destination)

    def test_other_source_tree_is_rejected_before_pages_download(self):
        run = {'status': 'completed', 'conclusion': 'success', 'repository': {'full_name': pages.REPO},
               'path': '.github/workflows/pages.yml', 'event': 'pull_request', 'head_sha': 'a' * 40, 'run_attempt': 1}
        proof = {'repository': pages.REPO, 'run_id': 42, 'attempt': 1, 'source_sha': 'a' * 40,
                 'source_tree': 'b' * 40}
        artifact = {'name': 'pages-source-42-1', 'expired': False}
        with patch.object(pages, 'api', side_effect=[run, {'artifacts': [artifact]}]), \
                patch.object(pages, 'archive', return_value=proof):
            with self.assertRaisesRegex(ValueError, 'anderen Quellbaum'):
                pages.validated('42', 'c' * 40)

    def test_executed_workflow_tree_must_match_the_checked_out_source(self):
        metadata = {'workflow_run': {'id': 42}, 'expired': False}
        with patch.dict(os.environ, {'GITHUB_RUN_ID': '42', 'PAGES_WORKFLOW_SHA': 'd' * 40}), \
                patch.object(pages.subprocess, 'check_output', side_effect=['a' * 40, 'b' * 40]), \
                patch.object(pages, 'api', side_effect=[metadata, {'commit': {'tree': {'sha': 'c' * 40}}}]):
            with self.assertRaisesRegex(ValueError, 'ungeprüfte Basisänderungen'):
                pages.record('7')


if __name__ == '__main__':
    unittest.main()
