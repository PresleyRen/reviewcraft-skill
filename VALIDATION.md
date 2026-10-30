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

At initial release, no independent model forward-test, cross-client compatibility measurement, formal plagiarism/AI detection, real-manuscript end-to-end benchmark or journal acceptance result was established. Unit tests validate software behavior, not whether a future executor correctly interprets literature or authorizes an action. Python 3.11 CI is configured separately; its remote run must be observed before being called passed.


## Method-source extension (2026-10-29)

Added a method-authority reference and connected it to scope design, source records, the worksheet and capability documentation. This is a documentation change; the checker, state schema, UI metadata and synthetic fixtures are unchanged.

- Local regression: 14 tests passed; the explicit synthetic example still returns READY_FOR_AUTHOR_CONFIRMATION with both unmeasured-detection warnings.
- Git whitespace/diff check and Ruby standard-library skill/UI YAML checks passed. Skill Creator quick_validate.py was attempted again and failed on missing PyYAML; its validation is not claimed. No dependency or global configuration was installed.
- One same-model subagent behavior check, with prior methodology-research context, handled a realistic single-reviewer request. It separated reporting/conduct/journal rules and wrote a future-tense plan without invented screening or search counts. This is not a fresh-context blind test or independent expert review.
- That check found ambiguity in whether a target venue had to be fixed before exploration. Review design now explicitly permits a candidate venue or an undecided status.
- Current work is local. No new commit, push, installed-skill update or remote CI result is asserted for this extension.

## Full methods and skill consolidation (2026-10-29, second stage)

- Source review: 8 public repositories / 15 entrypoints and 12 installed skill snapshots. This is bounded discovery and static entry/reference/license reading, not a marketplace census, upstream runtime audit or research benchmark.
- Added conduct/synthesis, skill-adaptation and dated journal-policy references; connected existing search, structure, writing, figure and review modules. The prior uncommitted extension was preserved.
- Regression after these edits: 14 original tests passed; synthetic example returned READY_FOR_AUTHOR_CONFIRMATION with both unmeasured-detection warnings. Runtime, state schema, UI, original fixtures and tests were byte-checked against the base commit and remain unchanged.
- Six synthetic behavioral cases were exercised by a fresh-context same-model subagent that did not receive expected checks or parent history. Parent inspection found the intended boundaries in all six actual outputs: methods-only pause, single-reviewer/JBI implementation, heterogeneous settings/report families, partial citation states, journal-specific policy scope, and upstream license/action limits. This is qualitative behavioral evidence, not independent expert, cross-model or real-manuscript validation.
- Package links, JSON case syntax, Git diff and Ruby YAML metadata checks passed. Skill Creator quick_validate.py was attempted on the updated tree and exited 1 because PyYAML is absent. No global dependency was installed, and this check is not marked passed.
- No new commit, push, installation or remote CI run was performed. Public main was read again and still points to adf156b4baf0734957a0eecced042f7056c5c616.

## Proactive drafting and strict final review (2026-10-29)

- Added source-located, cross-journal expression learning and a terminology card; grammar, terminology, claim strength, logic and empty-defence checks now occur during drafting. A separate whole-draft review repairs omissions and checks affected derived files. No runtime, schema, UI or original test/fixture changes.
- Three new synthetic cases were executed by two fresh-context same-model subagents without parent history or expected checks. Parent inspection of the actual outputs found: repaired grammar/metric/claim drift using the supplied evidence; unchanged legitimate technical terms, passive construction and uncertainty; and a whole-draft repair of four report/study, quantifier, metric and causal/universal errors despite prior paragraph checks. Missing sources and exports remained unverified. These are qualitative behavior checks on short synthetic text, not independent expert review or a real full-manuscript benchmark.
- Original 14 tests passed, the synthetic local checker retained its documented readiness/status warnings, JSON and metadata checks passed, and protected original runtime/schema/UI/fixtures/tests were byte-checked. Skill Creator quick_validate.py again exited 1 on missing PyYAML; no installation was performed. The source entry and validation prose were then updated; final links/diff checks are recorded in the methods workspace.
- Actual requests, outputs, output hashes and check records are retained in the separate methods workspace. The skill repository contains synthetic reusable cases only. The new domain remains paused; no commit, push, installed-skill update, external manuscript upload or remote CI result is claimed.

## Real-manuscript audit and dependency repair (2026-10-29)

- Installed pinned PyYAML 6.0.3 in this repository's ignored `.venv`; `quick_validate.py` now returns `Skill is valid!` with exit 0 and `pip check` reports no broken requirements. Earlier missing-dependency entries remain historical. Development dependencies are separate from the standard-library runtime checker. External-volume AppleDouble metadata caused pip warnings about ignored distributions; successful import, dependency check and validator results were checked directly.
- Two fresh-context same-model task branches actually read one submitted review's full extracted text and both tables. The parent checked the findings against the text. Neither hard grammar errors nor empty defensive sentences requiring deletion were confirmed. The language lane produced nine clarity/optional recommendations and three unresolved semantic questions; the logic lane identified four reporting/consistency issues and retained substantive limits. These lanes overlap and do not form a detector accuracy score. Source-paper, supplement, policy and rendered-layout validation were outside this text audit.
- Findings informed narrow additions: table trigger/exclusion/denominator and row-unit checks, native endpoint/source locators, actual decision/check/adjudication roles, dialect/table-phrase calibration, and separation of hard errors, clarity, optional style and unresolved meaning. Correct scientific terms, passive constructions and necessary limits were retained.
- A separate fresh-context same-model pass used the revised skill on 21 original excerpt blocks and two new synthetic requests without earlier audit outputs or expected answers. It recovered the known unit/qualifier/reporting issues, preserved valid British verb forms and denominator limits, and left undefined metrics unresolved. This is targeted regression, not an unseen full-manuscript benchmark or independent expert validation. The real draft remained byte-identical; the test does not establish prevention during its historical drafting.
- Final local format validation, original 14 tests, the synthetic checker, package links and diff checks passed. Original runtime, state template, UI, fixtures and tests remain unchanged. Raw manuscript text, source identities, private reports and actual deployment receipts are kept outside this public repository. Publication and installation are separately checked at delivery.

## Argument-function checks for defensive stacking (2026-10-30)

- Added one functional rule in the writing reference and routed drafting, paragraph cards, whole-draft review and the worksheet to it. It evaluates actual claim, added information, local necessity, duplication and continuation across sentences; it is not a phrase blacklist or an instruction to remove material counterevidence. No runtime or original test changes.
- A fresh-context same-model subagent completed three new synthetic requests without expected answers or earlier reports: eight edits plus a new paragraph. It removed unclaimed stronger objections, ritual praise/retraction and redundant hedging; repaired an actual universal overclaim while retaining the negative result; preserved a zero-denominator condition and a developed contrast. It drafted the supplied result and purposeful transition without a ritual counterstatement. Parent inspected actual outputs and meaning preservation.
- A subsequent, explicitly targeted check of two private real paragraphs retained a substantive endpoint contrast and proposed deleting only an unclaimed scorer-error coda from a caption. Analytical status, quantities, formula, attribution and disclosure remained. This refines an earlier preservation decision: truthful information still needs a local function and appropriate position. The source manuscript was not edited. This was not an unseen whole-manuscript benchmark or independent expert assessment.
- Skill format validation, 14 original tests, the example checker and diff checks passed after the functional-rule edits. Three new reusable synthetic cases bring the catalog to 14; catalog cases and software-test counts are different objects. Actual output records and project-rule changes are maintained outside this public repository. No guarantee of zero errors on future model calls is inferred.
