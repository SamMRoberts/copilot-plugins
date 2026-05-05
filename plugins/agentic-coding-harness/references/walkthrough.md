# Harness Walkthrough

Use this reference for first-pass harness creation when the user has not already supplied all required answers.

Ask questions in small rounds. Do not force all answers into one prompt when the user is still orienting.

## Required Input Categories

1. Project or product name.
2. One-sentence project purpose.
3. Primary users or operators.
4. Work explicitly in scope for coding agents.
5. Work explicitly out of scope.
6. Changes requiring explicit human approval.
7. Major product domains or app areas.
8. Architecture layers or dependency boundaries.
9. Language, framework, runtime, and package manager conventions.
10. Format, lint, test, build, typecheck, and startup commands.
11. Local app, UI, log, metric, trace, or validation workflows.
12. Security, privacy, reliability, or compliance constraints.
13. Locations for design docs, execution plans, app specs, and references.
14. Plan and technical-debt maintenance rules.
15. Quality or taste invariants agents must enforce.

## Drafting Rules

- Keep `AGENTS.md` compact and map-like.
- Put durable project knowledge in `docs/`.
- Make scope and refusal behavior explicit.
- Prefer exact commands and file paths over generic process text.
- Convert recurring failures into docs, scripts, tests, linters, hooks, or CI checks where practical.
