import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_review', REPO / 'scripts/check_review.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ReviewGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'paper.md').write_text('Synthetic review; not a real paper.\n')
        (self.root / 'audit.md').write_text('Synthetic audit fixture; no real review was done.\n')
        sha = checker.digest(self.root / 'paper.md')
        self.state = {
            'schema_version': 1,
            'manuscript': {'path': 'paper.md', 'sha256': sha},
            'files': [{'path': x, 'sha256': checker.digest(self.root / x)} for x in ('paper.md', 'audit.md')],
            'checks': {x: {'status': 'passed', 'manuscript_sha256': sha, 'evidence': ['audit.md']} for x in checker.CHECKS},
            'detection': {x: {'required': False, 'status': 'not_requested', 'reason': 'Not requested in this synthetic test.', 'score_percent': None, 'threshold_percent': None} for x in ('ai', 'similarity')},
            'submission': {'status': 'not_submitted'},
        }

    def result(self):
        return checker.validate(self.root, self.state)

    def test_good_synthetic_record_and_read_only(self):
        before = {f.name: f.read_bytes() for f in self.root.iterdir()}
        self.assertEqual(self.result()['status'], 'READY_FOR_AUTHOR_CONFIRMATION')
        self.assertEqual(before, {f.name: f.read_bytes() for f in self.root.iterdir()})

    def test_changed_manuscript_invalidates_hash(self):
        (self.root / 'paper.md').write_text('Changed text')
        self.assertTrue(self.result()['errors'])

    def test_old_full_review_does_not_approve_new_manuscript(self):
        self.state['checks']['full_review']['manuscript_sha256'] = '0' * 64
        self.assertTrue(any('full_review' in x for x in self.result()['errors']))

    def test_pass_without_evidence_rejected(self):
        self.state['checks']['references']['evidence'] = []
        self.assertTrue(any('references' in x for x in self.result()['errors']))

    def test_required_detection_not_done_rejected(self):
        self.state['detection']['ai']['required'] = True
        self.assertTrue(any('required detection' in x for x in self.result()['errors']))

    def test_unmeasured_is_not_zero(self):
        self.state['detection']['similarity']['score_percent'] = 0
        self.assertTrue(any('must be null' in x for x in self.result()['errors']))

    def detection_record(self):
        return {'required': True, 'status': 'completed', 'tool': 'Synthetic fixture only', 'date': '2026-01-01', 'settings': {}, 'manuscript_sha256': self.state['manuscript']['sha256'], 'report_path': 'audit.md', 'score_percent': 12, 'threshold_percent': 10}

    def test_threshold_and_real_report_required(self):
        self.state['detection']['ai'] = self.detection_record()
        self.assertTrue(any('exceeds' in x for x in self.result()['errors']))
        self.state['detection']['ai']['score_percent'] = 9
        self.assertFalse(self.result()['errors'])
        self.state['detection']['ai']['report_path'] = 'missing.txt'
        self.assertTrue(self.result()['errors'])

    def test_invalid_boolean_and_nonfinite_score_rejected(self):
        self.state['detection']['ai'] = self.detection_record()
        for bad in [True, float('nan'), float('inf'), -1, 101]:
            self.state['detection']['ai']['score_percent'] = bad
            self.assertTrue(self.result()['errors'])

    def test_no_evidence_path_traversal_or_symlink_escape(self):
        self.state['checks']['full_review']['evidence'] = ['../outside.md']
        self.assertTrue(self.result()['errors'])
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / 'secret.txt'
            external.write_text('Synthetic outside-root fixture')
            (self.root / 'outside.txt').symlink_to(external)
            self.state['files'].append({'path': 'outside.txt', 'sha256': checker.digest(external)})
            self.assertTrue(any('inside' in x for x in self.result()['errors']))

    def test_cannot_skip_full_review(self):
        self.state['checks']['full_review'] = {'status': 'not_applicable', 'reason': 'Already uploaded'}
        self.assertTrue(any('full_review' in x for x in self.result()['errors']))

    def test_no_receipt_no_confirmed_submission_record(self):
        self.state['submission'] = {'status': 'submitted', 'receipt_path': 'missing.json', 'manuscript_sha256': self.state['manuscript']['sha256']}
        self.assertTrue(any('submission:' in x for x in self.result()['errors']))

    def test_blank_template_is_not_ready(self):
        template = json.loads((REPO / 'templates/project-state.json').read_text())
        self.assertEqual(checker.validate(self.root, template)['status'], 'NEEDS_WORK')


class PackageTests(unittest.TestCase):
    def test_internal_markdown_links_resolve(self):
        for file in REPO.rglob('*.md'):
            if any(part.startswith('.') for part in file.relative_to(REPO).parts):
                continue  # macOS volumes may add binary ._ companion files.
            for target in re.findall(r'\]\(([^)\s]+)\)', file.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((file.parent / target.split('#')[0]).exists(), (file, target))

    def test_example_is_explicitly_synthetic_and_runnable(self):
        root = REPO / 'examples/synthetic-review'
        state = json.loads((root / 'project-state.json').read_text())
        self.assertIn('synthetic', (root / 'manuscript.md').read_text().lower())
        self.assertEqual(checker.validate(root, state)['status'], 'READY_FOR_AUTHOR_CONFIRMATION')


if __name__ == '__main__':
    unittest.main()
