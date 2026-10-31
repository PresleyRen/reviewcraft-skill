---
name: reviewcraft
description: "Plan and execute evidence-grounded literature reviews, systematic maps and survey manuscripts through journal selection, source reading, synthesis, English writing, Chinese translation, paragraph-level editing, figures, reviewer-style audit and submission preparation. Use for 写综述、综述方法与能力整合、逐段逻辑图、中英文稿同步、综述投稿检查; resume the current stage rather than restarting research."
license: MIT
---

# ReviewCraft

Turn a review question and original sources into a traceable synthesis and a journal-specific submission package. Work in the user's language; preserve the agreed manuscript language and authoritative version.

## Start from the actual state

Read the project's local rules, current status, current-file manifest and the requested artifacts. Determine review type, scope, target venue, resources and authorized action. Reuse completed evidence. A request to review authorizes inspection and findings; a request to revise authorizes the relevant changes; uploading, publishing research data and formally submitting are separate actions with their own actual authorization.

Keep one current manuscript, derived translations/exports, a small decision ledger and a file manifest. Respect separately owned experiment and review tasks. Do not impose this repository's template when the project already has equivalent records.

If the user requests methods research or skill consolidation first, complete that deliverable and preserve any pause on domain search, pilot extraction or manuscript writing. Do not automatically advance to the next research stage. Integrate useful capabilities by stage, rather than loading or installing every candidate skill.

## Route to the needed stage

| Stage | Read | Produce |
|---|---|---|
| Study review methods or consolidate skills | [Skill adapters](references/skill-adapters.md), [Conduct and synthesis](references/conduct-and-synthesis.md) | An audited capability map, source/permission decisions and tested skill changes |
| Choose scope and review type; compare venues | [Method authority](references/method-authority.md), [Review design](references/review-design.md), then relevant parts of [Conduct and synthesis](references/conduct-and-synthesis.md) | A bounded question, nearest-review difference and verified venue fit |
| Search, read, select and code | [Search and evidence](references/search-and-evidence.md) | Executed query log, dispositions, report-family links and source-located evidence |
| Build the argument, sections and paragraphs | [Structure and synthesis](references/structure-and-synthesis.md) | Question-to-conclusion map, section/paragraph logic and cross-study synthesis |
| Learn field expression, draft/edit English or synchronize Chinese | [Writing and bilingual work](references/writing-and-bilingual.md) | Source-located expression principles, checked paragraphs and synchronized translations |
| Prepare figures, references and files | [Figures and artifacts](references/figures-and-artifacts.md) | Numbered editable figures, checked citations and rendered outputs |
| Review, prepare uploads or handle revisions | [Review and submission](references/review-and-submission.md) | Located issues, actual check outcomes, journal package and appropriate status |
| Diagnose a stalled or repeated failure | [Lessons](references/lessons.md) | Root cause, narrow correction, counterexample and stopping decision |

Use [the worksheet](templates/review-worksheet.md) for a new project; [capability coverage](references/capability-coverage.md) maps concrete requests to modules. Methodological and publisher links are in [sources](references/sources.md). Read only the relevant modules. Existing specialist skills can help with editing, figures, documents or review when installed; this skill has no mandatory model, paid service or third-party skill dependency.

## Work with evidence, not a desired verdict

- Classify journal requirements, reporting guidelines, conduct methods and practice advice before applying them. PRISMA describes reporting; it does not establish review conduct quality. Match the review type and journal rather than assuming a universal SCI format.
- Report actual screeners, independence, automation and checks; model agreement or role simulation is not independent human screening.
- Every important synthesis must have a source version, reading depth, locator, scope and uncertainty. Identity verification is separate from claim support. An abstract is not a full-method reading.
- Distinguish records, reports, report families, datasets and independent experiments. Unretrieved, unread and unresolved are different outcomes. Keep them in the denominator appropriate to the stated count.
- Seek both supporting and contradicting sources. New taxonomy names or more paper counts do not by themselves establish a contribution. State the decision or understanding enabled by the synthesis.
- When searching stops under a budget, say so. Inspect whether later additions alter central categories or recommendations before claiming stable coverage. Do not turn a bounded map into an exhaustive survey by changing its title.
- Review the central case before editing style. Keep real limitations, counterevidence, required declarations and accurate AI-use information; remove empty defensive language and internal production chatter from the manuscript.
- Apply the [argument-function test](references/writing-and-bilingual.md#以论证功能清除叠加防御) while drafting and reviewing. End a supported explanation naturally; do not append imagined objections, stronger claims the text never made, ritual praise-then-retraction or repeated disclaimers. Internal critique calibrates the final argument; it is not manuscript narration.
- Learn terminology and argument moves from relevant reviews across journals. Check grammar, terminology, claim strength and paragraph logic while drafting; then perform a separate whole-manuscript review. Observed phrasing is a reference, not a journal rule or a sentence template.
- Use the [action, definition and context checks](references/writing-and-bilingual.md#用动作定义和上下文检查表达) when prose hides an operation, invents an unexplained compound, stacks empty modifiers or loses its context. Preserve established terms and meaningful qualifiers; an editor's paraphrase check is not a new human study.
- Use actual completed author contributions and approvals. A proposed task is not a completed CRediT role. A private repository draft is not a public deposit.

## Check before release

Complete the content/reviewer pass before uploading. Verify sources, table/figure numbers, actual SVG editability, PDF/DOCX renderings, translation meaning and the target journal's current instructions. Any later change must recheck the affected claims and derived artifacts.

Similarity checking and AI-text detection are separate optional or venue-required services. Record their actual status, tool, report, settings, date and manuscript hash. Without a report, the percentage is unknown. Style editing cannot measure or guarantee a detector score. Do not transmit an unpublished manuscript to an additional service without the user's relevant authorization.

The optional local checker accepts [project-state.json](templates/project-state.json):

```sh
python3 scripts/check_review.py --root /path/to/review --state project-state.json
```

It reads declared artifacts, hashes, evidence references and status fields. It does not search papers, interpret scientific truth, detect plagiarism/AI authorship, upload, pay or submit. Its success means `READY_FOR_AUTHOR_CONFIRMATION`, not acceptance or submission. See [the synthetic example](examples/README.md) for a runnable demonstration.

## Report each turn simply

```text
本次做了什么 → 得到什么结论 → 下一步做什么 → 预期解决什么
```

Add a short text flow when it helps; link detailed records rather than repeating them. State what was actually checked and the remaining decision-changing gap. When a stage fails, retain the reason and reopen condition; do not endlessly rephrase the same failed route.
