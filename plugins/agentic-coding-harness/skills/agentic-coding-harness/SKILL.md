---
name: agentic-coding-harness
description: Create, initialize, update, and enforce an agentic coding harness: a short AGENTS.md table of contents, docs/ knowledge base, execution plans, app specs, reference docs, and scope guardrails. Use when the user asks to build or maintain a harness, initialize repo instructions, audit harness compliance, or decide whether proposed code changes are in scope. Do not use for ordinary feature work unless the task may conflict with the harness.
---

# Agentic Coding Harness Skill

Use this skill to create, update, maintain, or validate a repository-local coding harness that makes the codebase legible and safe for coding agents.

A harness is not a long instruction manual. It is a compact routing layer plus versioned documentation, plans, scope boundaries, and validation rules that agents must follow before changing code.

## Operating principles

1. Keep `AGENTS.md` short, stable, and table-of-contents oriented.
2. Put durable knowledge in `docs/`, not in a monolithic instruction file.
3. Treat repository-local markdown, schemas, scripts, tests, and generated docs as the agent-visible system of record.
4. Use progressive disclosure: read the smallest relevant docs first, then branch to deeper docs based on task context.
5. Prefer mechanical enforcement through tests, linters, scripts, and CI over prose-only rules.
6. Encode human taste as reusable invariants and docs updates, not one-off comments.
7. Never change code when the requested work conflicts with, exceeds, or is absent from the harness scope.

## Required output layout for a target repository

Create or update this structure:

```text
AGENTS.md
docs/
  README.md
  harness/
    scope.md
    initialization.md
    operating-model.md
  design-docs/
    index.md
    core-beliefs.md
  exec-plans/
    index.md
    plan-template.md
    tech-debt-tracker.md
    active/
      README.md
    completed/
      README.md
  app-specs/
    index.md
    app-spec.md
  references/
    index.md
  architecture.md
  tooling.md
  quality.md
  security.md
  reliability.md
  observability.md
  review.md
```

Additional docs may be added under `docs/`, but do not move design docs, execution plans, app specs, or reference docs outside `docs/`.

## Initialization workflow

When creating a harness from scratch, use the bundled initializer when available:

```bash
python /path/to/agentic-coding-harness/scripts/init_harness.py
```

If this plugin is installed under a repository-local plugin folder, the command is usually:

```bash
python .agents/plugins/agentic-coding-harness/scripts/init_harness.py
```

The script asks the user a guided series of questions and writes `AGENTS.md` plus the `docs/` skeleton. If running scripts is not possible, ask the same questions manually and create the files yourself.

### Initialization questions

Ask these questions in order unless the answer is already present in the repo or user prompt:

1. What is the project or product name?
2. What does the project do in one sentence?
3. Who are the primary users or operators?
4. What work is explicitly in scope for coding agents?
5. What work is explicitly out of scope?
6. What changes require explicit human approval?
7. What are the major product domains or app areas?
8. What architecture layers or dependency boundaries must be preserved?
9. What language, framework, runtime, and package manager conventions apply?
10. What commands validate formatting, linting, tests, builds, and type checks?
11. What local app startup, UI, observability, log, or metric workflows should agents use?
12. What security, privacy, reliability, or compliance constraints are non-negotiable?
13. Where should design docs, execution plans, app specs, and references be filed?
14. How should active plans, completed plans, and technical debt be maintained?
15. What are the top quality or “taste” invariants the agent should enforce?

## Scope gate before any code change

Before editing code, perform this gate:

1. Read `AGENTS.md`.
2. Read `docs/harness/scope.md`.
3. Use the `AGENTS.md` table of contents to read docs relevant to the task.
4. Classify the task as one of:
   - `IN_SCOPE`: covered by harness scope and not conflicting.
   - `NEEDS_PLAN`: in scope but complex enough to require an execution plan.
   - `HARNESS_UPDATE_REQUIRED`: useful work, but current harness does not include it.
   - `OUT_OF_SCOPE`: explicitly excluded by the harness.
   - `CONFLICTS_WITH_HARNESS`: contradicts architecture, product, security, reliability, quality, or process constraints.
5. Only proceed with code edits for `IN_SCOPE` or after creating/reading a valid plan for `NEEDS_PLAN`.

## Non-negotiable refusal rule

Never make code changes that:

- conflict with the harness;
- are explicitly out of scope per the harness;
- are not included in the harness scope;
- bypass required validation, planning, or approval steps;
- move durable harness knowledge outside `docs/`;
- alter the scope gate itself to make an unrelated task appear allowed.

When a request fails the scope gate, do not patch code. Respond with:

```text
Harness gate blocked this change.
Reason: <specific doc/rule that blocks it>
Resolution options:
1. Update the harness scope/docs, then create a new plan.
2. Stop this task with no changes.
3. Create a new in-scope plan that satisfies the current harness.
```

If the user chooses to update the harness, update documentation first. Do not implement the originally blocked code change until the updated harness clearly permits it.

## Planning rules

Create or update an execution plan in `docs/exec-plans/active/` when work spans multiple files, changes architecture, touches security/reliability behavior, alters user-visible behavior, or carries unclear acceptance criteria.

A plan must include:

- task summary;
- in-scope and out-of-scope boundaries;
- docs consulted;
- intended files and interfaces;
- validation commands;
- risks and rollback notes;
- progress log;
- decisions made during execution.

Move completed plans to `docs/exec-plans/completed/` after implementation and validation.

## Documentation update rules

For every harness-affecting change:

1. Update the most specific doc in `docs/`.
2. Update indexes when adding, moving, or retiring docs.
3. Keep `AGENTS.md` as a routing table, not an encyclopedia.
4. Prefer creating a specific doc over expanding `AGENTS.md`.
5. Record stale docs or missing invariants in `docs/exec-plans/tech-debt-tracker.md`.

## Validation rules

After creating or updating a harness:

1. Check that `AGENTS.md` is around 100 lines.
2. Confirm `AGENTS.md` has a table of contents routing tasks to docs.
3. Confirm design docs, execution plans, app specs, and references live under `docs/`.
4. Confirm `docs/harness/scope.md` has explicit in-scope, out-of-scope, and approval-required sections.
5. Confirm the scope gate text appears in both `AGENTS.md` and `docs/harness/scope.md`.
6. Confirm validation commands are captured in `docs/tooling.md`.
7. Confirm architecture constraints are captured in `docs/architecture.md`.

Use this command to inspect the generated `AGENTS.md` line count:

```bash
python - <<'PY'
from pathlib import Path
p = Path('AGENTS.md')
print(len(p.read_text().splitlines()), 'lines')
PY
```

When available, run the bundled validator from the repository root:

```bash
python /path/to/agentic-coding-harness/scripts/validate_harness.py
```

For a repository-local plugin install, the command is usually:

```bash
python .agents/plugins/agentic-coding-harness/scripts/validate_harness.py
```

## Harness maintenance workflow

When updating an existing harness:

1. Read `AGENTS.md` and `docs/README.md`.
2. Read `docs/harness/scope.md`.
3. Identify whether the change is a routing update, scope update, plan update, architecture update, app-spec update, reference update, or enforcement update.
4. Modify the smallest set of docs needed.
5. Keep cross-links current.
6. Avoid creating duplicate sources of truth.
7. If docs and code disagree, document the discrepancy and ask whether to update docs, update code, or open a new plan.

## Mechanical enforcement suggestions

When the repository supports it, add or propose:

- dependency-boundary tests;
- custom lint rules for architecture and naming invariants;
- file size or layer import checks;
- schema or boundary validation tests;
- documentation link checks;
- stale-doc detection;
- CI checks that fail when scope docs, indexes, or plan metadata are malformed.

Do not invent tooling that the repository cannot run. Put proposed future checks in `docs/exec-plans/tech-debt-tracker.md`.

## References

Load these only when needed:

- `../../references/harness-engineering-notes.md`: design rationale.
- `../../references/repository-docs-structure.md`: required generated docs and acceptable extensions.
- `../../references/walkthrough.md`: guided interview and drafting flow.
- `../../references/examples.md`: example outputs and answer-file shape.
