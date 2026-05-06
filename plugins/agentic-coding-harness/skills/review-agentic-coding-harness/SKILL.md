---
name: review-agentic-coding-harness
description: Review an existing or generated agentic coding harness for completeness, specificity, consistency, and readiness. Use when the user asks to audit, review, score, validate section quality, or create section-state review files for a harness. Produces one file per section named <section_name>.<state>.md where state is complete, needs_update, or failed. Do not rewrite the harness unless the user also asks for refinement.
---

# Review Agentic Coding Harness

Use this skill to evaluate a coding harness section by section and create review artifacts that can drive refinement.

## Inputs

- Harness content or path, usually `AGENTS.md` plus `docs/`.
- Target repository context.
- Validation directory, defaulting to `.harness-validation/`.
- Optional custom section list.
- User-specific quality bar or constraints.

## Procedure

1. Read `AGENTS.md`, `docs/README.md`, and `docs/harness/scope.md` when present.
2. Load `../../references/section-refinement.md` for state rules and required sections.
3. Load `../../references/repository-docs-structure.md` when evaluating knowledge-system coverage.
4. Evaluate each section independently for specificity, consistency, paths, commands, boundaries, evidence, and stop conditions.
5. Create exactly one review file per section named `<section_name>.<state>.md`.
6. Include current content, review notes, missing details, and recommended next action in each section file.
7. Run the section status script from the repository root when available:

```bash
python /path/to/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

For a repository-local plugin install, the command is usually:

```bash
python .agents/plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

## State Rules

- `complete`: specific, internally consistent, and usable by another agent without hidden context.
- `needs_update`: mostly correct but needs clearer paths, commands, boundaries, examples, or sequencing.
- `failed`: wrong, generic, contradictory, unsafe, or better regenerated from scratch.

## Output

Return:

- validation directory used;
- counts for `complete`, `needs_update`, and `failed`;
- next action from the status script;
- global issues affecting multiple sections;
- whether the harness is ready for refinement or already complete.
