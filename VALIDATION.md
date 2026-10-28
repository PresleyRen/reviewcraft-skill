# Validation record

This record covers the repository software and packaging, not the scientific quality of a manuscript.

Initial local test run: 13 tests passed and one package-link test errored because the external macOS volume created binary AppleDouble (`._`) companion files. The reader now excludes hidden metadata from Markdown-link checks, matching the release file selection. No scientific expectation or score was changed.

## Final local checks (2026-10-29)

- `python3 -m unittest discover -s tests -v`: 14 tests passed on Python 3.14. Tests cover changed files, stale full-review evidence, missing evidence/reports, required-but-unavailable detection, unknown-vs-zero, thresholds, invalid scores, traversal/symlink escape, submission receipt records, an incomplete template, package links and the synthetic example.
- `python3 scripts/check_review.py --root examples/synthetic-review --state project-state.json`: READY_FOR_AUTHOR_CONFIRMATION, 2 fixture files checked; both detection warnings explicitly say no measured percentage.
- Skill and UI YAML parsed using Ruby standard-library YAML; skill name, description and invocation target checked. Result: PASS_SKILL_METADATA_YAML.
- The bundled Skill Creator `quick_validate.py` was attempted but could not run because its Python environment has no PyYAML. No global package was installed; the separate YAML/link checks above are the checks actually completed, not a claim that the bundled validator passed.
- Release content is selected from a fixed allowlist, inspected for private paths, access links and secrets, and contains only original documentation/code plus synthetic fixtures. The unpublished manuscript and source-project records are not copied.

## Not established

No independent model forward-test, cross-client compatibility measurement, formal plagiarism/AI detection, real-manuscript end-to-end benchmark or journal acceptance result is claimed. Unit tests validate software behavior, not whether a future executor correctly interprets literature or authorizes an action. Python 3.11 CI is configured separately; its remote run must be observed before being called passed.

