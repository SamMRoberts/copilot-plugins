# Review Checklist

Detailed criteria for each review area. Load the relevant section on demand.

## Frontmatter

| Field | Rule |
|---|---|
| `name` | Lowercase alphanumeric + hyphens only. 1–64 characters. Must match folder name exactly. |
| `description` | Present. Under 1024 characters. Must use imperative phrasing ("Use when…"). |
| `argument-hint` | Present when `user-invocable: true`. |
| `user-invocable` | Set intentionally. Delegation-only skills should be `false`. |
| `disable-model-invocation` | Only set to `true` if the skill should never auto-load. Rarely needed. |

## Description Quality

A good description:
- Uses imperative phrasing: "Use this skill when…" not "This skill does…"
- Focuses on user intent, not internal mechanics.
- Lists specific domains, formats, and trigger phrases — including cases where the user may not name the domain directly.
- States what the skill does NOT cover when there are adjacent capabilities that could cause false triggers.
- Is concise: a few sentences to a short paragraph.

A poor description:
- Is vague ("A helpful skill for tasks").
- Only describes what the skill does, not when the agent should reach for it.
- Does not include keywords a user would actually type.
- Exceeds 1024 characters.

## Context Efficiency

Cut if:
- The agent already knows it without being told (what a PDF is, how HTTP works, what a migration does).
- It adds no actionable constraint (generic advice like "handle errors appropriately").
- It duplicates a sub-skill's responsibility.

Move to references/ if:
- It is a long output template only needed at render time.
- It is a detailed lookup table or reference doc used only in specific cases.
- It is rarely-needed edge case detail that would waste context on normal runs.
- The file exceeds 500 lines / 5000 tokens with it included.

Keep in SKILL.md if:
- It is a gotcha the agent will encounter before recognizing the trigger (e.g., "Table X uses soft deletes — always add WHERE deleted_at IS NULL").
- It is a short output template (under ~20 lines) used on every run.
- It is a procedure step the agent needs on every invocation.

## Procedure Quality

Good procedure steps:
- Describe how to approach a class of problems (reusable method), not what to answer for one specific case.
- Give a clear default when multiple tools or approaches are valid.
- Mention alternatives briefly rather than presenting equal options.
- Include concrete gotchas — environment-specific facts that defy reasonable assumptions.
- Use validation loops for multi-step workflows (do → validate → fix → repeat).

Weak procedure steps:
- Tell the agent what to produce without explaining how to get there.
- Present multiple options without a default ("you can use A, B, or C").
- Include general advice instead of concrete corrections ("handle edge cases appropriately").
- Are over-prescriptive where flexibility is fine (e.g., exact phrasing when any clear wording works).
- Are under-prescriptive where a specific sequence must be followed.

## Structure and File Organization

- SKILL.md body should be under 500 lines and 5000 tokens.
- Output format templates over ~20 lines → move to `assets/` or `references/`.
- Reusable logic that appears in multiple steps → move to `scripts/`.
- Detailed reference material loaded conditionally → move to `references/` with explicit load trigger.
- Always use relative paths (`./scripts/`, `./references/`) for bundled resources.

## Script Design

Scripts bundled in `scripts/` must be agentic-safe:

- No interactive prompts (TTY blocks hang indefinitely in agent environments).
- All input via flags, environment variables, or stdin — never interactive.
- `--help` output documents flags, description, and usage examples concisely.
- Clear, actionable error messages (state what was wrong, what was expected, what to try).
- Structured output (JSON, CSV, TSV) on stdout; diagnostics on stderr.
- Pin dependency versions (e.g., `npx eslint@9.0.0`, `uvx ruff@0.8.0`) for reproducibility.
- Support `--dry-run` for destructive or stateful operations.
- Use distinct exit codes for different failure types.
- Default to summary output for large results; support `--offset` or `--output FILE` for pagination.
- Idempotent where possible ("create if not exists" over "create and fail on duplicate").

## Eval Readiness

A well-evaluated skill has:
- `evals/evals.json` with 2–3+ test cases, each containing:
  - `prompt`: realistic user message (casual phrasing, real file paths, personal context).
  - `expected_output`: human-readable description of success.
  - `assertions`: verifiable pass/fail statements about output (avoid vague or overly brittle assertions).
  - `files` (optional): input files the skill needs.
- At least one edge case prompt (malformed input, unusual request, ambiguous instructions).
- Both should-trigger and should-not-trigger queries for description validation.

Highest-value test cases to create first:
- The most common use case at its most typical phrasing.
- The most failure-prone scenario (complex steps, external dependencies, ambiguous input).
- A near-miss negative case (shares keywords but should not trigger).
