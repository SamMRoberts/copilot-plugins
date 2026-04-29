---
name: review-agentic-coding-harness
description: "Use when evaluating an existing or generated agentic coding harness for completeness, specificity, correctness, internal consistency, and readiness. Produces section-level markdown review files named <section_name>.<state>.md where state is complete, needs_update, or failed. Do not rewrite the harness except to create review artifacts unless the user also asks for refinement."
argument-hint: "Provide the harness content or path, target repository context, validation directory, and any required section list."
---

# Review Agentic Coding Harness

Use this skill to evaluate a coding harness section by section and create state files that drive refinement.

Read `../create-agentic-coding-harness/references/section-refinement.md` for the state rubric and file naming rules.
Read `../create-agentic-coding-harness/references/agent-first-harness-principles.md` before evaluating whether the harness is agent-first enough.

## Inputs

- Harness content or path.
- Target repository or workflow context.
- Validation directory, defaulting to `.harness-validation/`.
- Required section list, defaulting to the standard harness sections.
- Any user-specific quality bar or constraints.

## Review Procedure

1. Read the harness and target context.
2. Identify the harness sections to evaluate.
3. Evaluate each section independently using the section refinement rubric and agent-first principles.
4. Create exactly one file per section using `<section_name>.<state>.md`.
5. Include the current section content, review notes, missing details, and recommended next action in each file.
6. Run the status script to confirm the validation directory has a coherent next action:

```bash
python3 plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

## State Rules

- Use `complete` when the section is specific, internally consistent, and usable without hidden context.
- Use `needs_update` when the section is mostly correct but needs clearer paths, commands, boundaries, examples, or sequencing.
- Use `failed` when the section is wrong, generic, contradictory, or would be safer to recreate from scratch.

## Agent-First Review Checks

Flag gaps when the harness does not:

- Treat repository-local, versioned artifacts as the system of record.
- Keep the agent entry point concise and map-like.
- Define deeper docs, plans, indexes, schemas, and freshness checks.
- Make application state, UI evidence, logs, metrics, traces, or other runtime signals inspectable by agents where relevant.
- Encode hard architecture, safety, quality, and taste rules mechanically.
- Use standard development tools directly instead of requiring human copy-paste.
- Define feedback loops for review comments, bugs, failed runs, stale docs, drift, and recurring cleanup.
- Preserve human judgment for ambiguous decisions while letting agents execute repeatable work.

## Output

Return:

- Validation directory used.
- Count of complete, needs_update, and failed sections.
- The next section action reported by the status script.
- Any global issues that affect multiple sections.
- Whether the harness is ready for refinement or already complete.
