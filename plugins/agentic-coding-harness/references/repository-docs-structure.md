# Repository Docs Structure

Use this reference when evaluating or creating the generated repository harness layout.

## Required Entry Point

- `AGENTS.md`: short routing map, close to 100 lines, with a scope gate and table of contents.

## Required Docs Tree

```text
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

## Acceptance Rules

- Design docs, execution plans, app specs, and references stay under `docs/`.
- `docs/harness/scope.md` must include explicit in-scope, out-of-scope, approval-required, and blocked-change response sections.
- `docs/tooling.md` must list validation commands or explicitly identify missing commands.
- Architecture, quality, security, reliability, observability, and review expectations must each have a clear source-of-truth doc.
- Indexes must list required folders and explain where new docs belong.
- Additional docs are allowed when they are linked from an index or `AGENTS.md`.
