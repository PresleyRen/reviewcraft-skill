import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

import yaml

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
    def test_skill_and_ui_metadata_are_valid(self):
        content = (REPO / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---(?:\n|$)', content, re.DOTALL)
        self.assertIsNotNone(match, 'SKILL.md requires YAML frontmatter')
        metadata = yaml.safe_load(match.group(1))
        self.assertIsInstance(metadata, dict)
        self.assertFalse(set(metadata) - {'name', 'description', 'license', 'allowed-tools', 'metadata'})
        for field in ('name', 'description'):
            self.assertIsInstance(metadata.get(field), str, field)
            self.assertTrue(metadata[field].strip(), field)
        name = metadata['name'].strip()
        self.assertRegex(name, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertLessEqual(len(name), 64)
        self.assertLessEqual(len(metadata['description'].strip()), 1024)
        self.assertNotRegex(metadata['description'], r'[<>]')

        ui = yaml.safe_load((REPO / 'agents/openai.yaml').read_text(encoding='utf-8'))
        self.assertIsInstance(ui, dict)
        interface = ui.get('interface')
        self.assertIsInstance(interface, dict)
        for field in ('display_name', 'short_description', 'default_prompt'):
            self.assertIsInstance(interface.get(field), str, field)
            self.assertTrue(interface[field].strip(), field)
        self.assertRegex(interface['default_prompt'], rf'\${re.escape(name)}(?![\w-])')

    def test_behavior_scenario_catalog_is_valid(self):
        catalog = json.loads((REPO / 'evals/scenarios.json').read_text(encoding='utf-8'))
        self.assertIsInstance(catalog, dict)
        self.assertIs(type(catalog.get('schema_version')), int)
        self.assertEqual(catalog['schema_version'], 1)
        self.assertIs(catalog.get('automatic_score'), False)
        cases = catalog.get('cases')
        self.assertIsInstance(cases, list)
        self.assertTrue(cases)
        ids = set()
        for case in cases:
            self.assertIsInstance(case, dict)
            with self.subTest(case=case.get('id')):
                for field in ('id', 'request'):
                    self.assertIsInstance(case.get(field), str, field)
                    self.assertTrue(case[field].strip(), field)
                self.assertNotIn(case['id'], ids, 'Scenario IDs must be unique')
                ids.add(case['id'])
                self.assertIsInstance(case.get('inspect'), list)
                self.assertTrue(case['inspect'])
                for item in case['inspect']:
                    self.assertIsInstance(item, str)
                    self.assertTrue(item.strip())

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
