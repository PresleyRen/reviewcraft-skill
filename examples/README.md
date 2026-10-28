# Runnable synthetic example

`synthetic-review/` contains a minimal fake manuscript and fake audit fixture. It demonstrates a structurally complete record. No real literature search, review, detector run or submission is claimed.

From the repository root:

```sh
python3 scripts/check_review.py --root examples/synthetic-review --state project-state.json
```

Expected: `READY_FOR_AUTHOR_CONFIRMATION`, with warnings that similarity and AI detection were not requested and have no measured percentages. This is software-fixture success, not scientific validation. Changing the manuscript without refreshing its actual review evidence must invalidate the gate. Copy the blank template, not this completed synthetic fixture, for real projects.
