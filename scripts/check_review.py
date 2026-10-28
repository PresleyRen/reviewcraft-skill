#!/usr/bin/env python3
"""Read-only review-artifact gate; no model calls, network, scoring or submission."""
import argparse
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
import sys

CHECKS = (
    'journal_policy', 'coverage', 'coding_reliability', 'synthesis',
    'full_review', 'references', 'figures', 'bilingual', 'rendered_files',
    'declarations',
)
NON_SKIPPABLE = {
    'journal_policy', 'coverage', 'synthesis', 'full_review', 'references',
    'rendered_files', 'declarations',
}
SHA256 = re.compile(r'[0-9a-f]{64}')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_file(root, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Expected a nonempty relative file path')
    rel = Path(value)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('File path must stay inside the review: ' + value)
    path = (root / rel).resolve(strict=True)
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Expected a file inside the review: ' + value)
    return path


def percent(value):
    return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 100


def validate(root, state):
    """Check declared evidence identity, not the truth of supplied review reports."""
    root = Path(root).resolve(strict=True)
    if not isinstance(state, dict) or state.get('schema_version') != 1:
        raise ValueError('Expected a schema_version=1 state object')
    errors, warnings, registered = [], [], {}
    entries = state.get('files')
    if not isinstance(entries, list):
        raise ValueError('files must be a list')
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append('Each files entry must be an object')
            continue
        name, sha = entry.get('path'), entry.get('sha256')
        try:
            path = local_file(root, name)
            if path in registered:
                raise ValueError('Duplicate registered file: ' + name)
            if not isinstance(sha, str) or not SHA256.fullmatch(sha):
                raise ValueError('Invalid SHA256: ' + str(name))
            if digest(path) != sha:
                raise ValueError('File hash mismatch: ' + name)
            registered[path] = sha
        except (ValueError, OSError) as exc:
            errors.append(str(exc))

    def evidence(value):
        path = local_file(root, value)
        if path not in registered:
            raise ValueError('Evidence file not registered with matching hash: ' + str(value))
        return path

    manuscript = state.get('manuscript')
    if not isinstance(manuscript, dict):
        raise ValueError('manuscript must be an object')
    target_sha = manuscript.get('sha256')
    try:
        path = evidence(manuscript.get('path'))
        if target_sha != registered[path]:
            errors.append('Manuscript SHA does not match its registered file')
    except (ValueError, OSError) as exc:
        errors.append('manuscript: ' + str(exc))

    checks = state.get('checks')
    if not isinstance(checks, dict):
        raise ValueError('checks must be an object')
    for name in sorted(set(checks) - set(CHECKS)):
        errors.append('Unknown check name: ' + name)
    for name in CHECKS:
        check = checks.get(name)
        if not isinstance(check, dict):
            errors.append(name + ': missing check object')
            continue
        status = check.get('status')
        if status == 'not_applicable':
            if name in NON_SKIPPABLE or not str(check.get('reason') or '').strip():
                errors.append(name + ': cannot skip this check without an applicable reason')
        elif status == 'passed':
            if check.get('manuscript_sha256') != target_sha:
                errors.append(name + ': review belongs to a different manuscript hash')
            refs = check.get('evidence')
            if not isinstance(refs, list) or not refs:
                errors.append(name + ': passed requires actual evidence files')
            else:
                for ref in refs:
                    try:
                        evidence(ref)
                    except (ValueError, OSError) as exc:
                        errors.append(name + ': ' + str(exc))
        else:
            errors.append(name + ': ' + str(status) + '; check not complete')

    detection = state.get('detection')
    if not isinstance(detection, dict):
        raise ValueError('detection must be an object')
    for name in ('similarity', 'ai'):
        record = detection.get(name)
        if not isinstance(record, dict):
            errors.append(name + ': missing detection status')
            continue
        required, status = record.get('required'), record.get('status')
        if type(required) is not bool:
            errors.append(name + ': required must be true or false')
        threshold = record.get('threshold_percent')
        if threshold is not None and not percent(threshold):
            errors.append(name + ': threshold must be between 0 and 100')
        if status == 'completed':
            if record.get('manuscript_sha256') != target_sha:
                errors.append(name + ': report belongs to a different manuscript hash')
            try:
                evidence(record.get('report_path'))
            except (ValueError, OSError) as exc:
                errors.append(name + ': ' + str(exc))
            score = record.get('score_percent')
            if not percent(score):
                errors.append(name + ': completed requires a real score between 0 and 100')
            elif percent(threshold) and score > threshold:
                errors.append(name + ': recorded score exceeds the configured threshold')
            if not isinstance(record.get('tool'), str) or not record['tool'].strip():
                errors.append(name + ': completed requires a tool name')
            try:
                date.fromisoformat(record.get('date'))
            except (TypeError, ValueError):
                errors.append(name + ': completed requires date YYYY-MM-DD')
            if not isinstance(record.get('settings'), dict):
                errors.append(name + ': settings must be an object')
        elif status in ('not_requested', 'unavailable'):
            if record.get('score_percent') is not None:
                errors.append(name + ': no completed report; score must be null, not zero')
            if not str(record.get('reason') or '').strip():
                errors.append(name + ': missing reason for absent detection')
            if required:
                errors.append(name + ': required detection is not complete')
            else:
                warnings.append(name + ': ' + status + '; no measured percentage')
        else:
            errors.append(name + ': unknown detection status ' + str(status))

    submission = state.get('submission')
    if not isinstance(submission, dict):
        raise ValueError('submission must be an object')
    if submission.get('status') == 'submitted':
        try:
            evidence(submission.get('receipt_path'))
        except (ValueError, OSError) as exc:
            errors.append('submission: ' + str(exc))
        if submission.get('manuscript_sha256') != target_sha:
            errors.append('submission: receipt record belongs to a different manuscript hash')
        warnings.append('Submission is user-recorded; portal truth and receipt contents require inspection')
    elif submission.get('status') not in ('not_submitted', 'draft_uploaded'):
        errors.append('Unknown submission status')
    return {
        'status': 'NEEDS_WORK' if errors else 'READY_FOR_AUTHOR_CONFIRMATION',
        'checked_files': len(registered), 'errors': errors, 'warnings': warnings,
        'recorded_submission_status': submission.get('status'),
        'scope': 'Declared files, hashes and evidence/status links only; no scientific, detection or portal verification',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--state', default='project-state.json')
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        state = json.loads(local_file(root, args.state).read_text(encoding='utf-8'))
        result = validate(root, state)
    except (ValueError, OSError) as exc:
        print(json.dumps({'status': 'NEEDS_WORK', 'errors': [str(exc)]}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result['errors']))


if __name__ == '__main__':
    sys.exit(main())
