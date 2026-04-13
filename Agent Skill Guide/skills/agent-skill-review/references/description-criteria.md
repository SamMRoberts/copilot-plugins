# Description Criteria

Use this reference to evaluate and improve the `description` field of a SKILL.md.

## How Triggering Works

At startup, agents load only the `name` and `description` of each available skill. The description is the sole signal the agent uses to decide whether to load the full SKILL.md. If the description doesn't convey when the skill is useful, the agent won't reach for it.

Skills are more likely to trigger on tasks that require specialized knowledge the agent can't handle alone — unfamiliar APIs, domain-specific workflows, multi-step procedures. Simple one-step requests may not trigger even with a matching description.

## Writing Criteria

| Criterion | Good | Weak |
|---|---|---|
| Phrasing | Imperative: "Use when…", "Use for…" | Declarative: "This skill does…" |
| Focus | User intent and task outcome | Internal mechanics and implementation |
| Coverage | Lists specific domains, formats, actions, and edge trigger phrases | Mentions only the main happy path |
| Exclusions | States what it does NOT cover when adjacent skills could false-trigger | No boundary stated |
| Length | A few sentences to a short paragraph | Either too terse (one phrase) or over 1024 characters |

## Trigger Breadth

A description should be pushy: explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly.

Example of insufficient coverage:
```
description: 'Analyze CSV files.'
```

Example of well-calibrated coverage:
```
description: >
  Analyze CSV and tabular data files — compute summary statistics, add derived
  columns, generate charts, and clean messy data. Use this skill when the user
  has a CSV, TSV, or Excel file and wants to explore, transform, or visualize
  the data, even if they don't explicitly mention "CSV" or "analysis."
```

## Near-Miss Exclusions

When a skill shares keywords with adjacent capabilities, add a brief exclusion to prevent false triggers.

Example:
```
description: '...Use for querying and reporting. Do not use for database schema migrations or DDL changes.'
```

## Optimization Loop

To test and improve trigger accuracy:

1. Write ~20 eval queries: 8–10 that should trigger, 8–10 that shouldn't.
2. Split into train (~60%) and validation (~40%) sets — keep the split fixed.
3. Run each query multiple times (3 runs is a reasonable baseline); compute trigger rate.
4. A should-trigger query passes if trigger rate > 0.5. A should-not-trigger query passes if trigger rate < 0.5.
5. Identify failures in the train set only. Revise the description to address the general category, not the specific failed query (avoid overfitting).
6. Repeat until train set passes or improvement plateaus (~5 iterations is usually enough).
7. Select the iteration with the best validation pass rate — not necessarily the last one.
8. Verify the final description is under 1024 characters.

## Strong Negative Test Cases

The most valuable negative queries are near-misses — they share keywords with the skill but need something different.

Weak negatives (too easy, tests nothing):
- `"Write a fibonacci function"` (no keyword overlap)
- `"What's the weather?"` (completely irrelevant)

Strong negatives (share concepts but should not trigger):
- For a CSV analysis skill: `"write a Python script that reads a CSV and uploads rows to Postgres"` — involves CSV but the task is ETL, not analysis.
- For a code review skill: `"refactor this function to use async/await"` — involves code quality concepts but the task is transformation, not review.
