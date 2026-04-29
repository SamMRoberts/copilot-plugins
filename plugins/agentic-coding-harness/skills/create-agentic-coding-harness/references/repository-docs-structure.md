# Repository Docs Structure

Use this as the default documentation structure for harness-generated repository knowledge systems unless the user explicitly chooses a different layout.

```text
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   ├── example-spec.md
│   └── ...
├── references/
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

## File Roles

- `AGENTS.md`: short agent entry point and map. Keep it concise and link to deeper docs.
- `ARCHITECTURE.md`: top-level architecture, layering, dependencies, and invariants.
- `docs/design-docs/index.md`: index of design docs and decision records.
- `docs/design-docs/core-beliefs.md`: durable agent-first principles, taste invariants, and operating beliefs.
- `docs/exec-plans/active/`: active plans for complex work.
- `docs/exec-plans/completed/`: completed plans and decision logs.
- `docs/exec-plans/tech-debt-tracker.md`: known debt and cleanup backlog.
- `docs/generated/db-schema.md`: generated database/schema reference; adapt name for non-database projects.
- `docs/product-specs/index.md`: index of product or feature specifications.
- `docs/product-specs/example-spec.md`: example format for future specs.
- `docs/references/`: external or long-form references copied into repository-local form.
- `docs/DESIGN.md`: design system, UX, and interface guidance.
- `docs/FRONTEND.md`: frontend architecture and verification guidance.
- `docs/PLANS.md`: planning conventions and plan lifecycle.
- `docs/PRODUCT_SENSE.md`: product judgment, user value, and prioritization guidance.
- `docs/QUALITY_SCORE.md`: quality rubric, quality grades, and improvement tracking.
- `docs/RELIABILITY.md`: reliability expectations, SLOs, observability, and incident lessons.
- `docs/SECURITY.md`: security boundaries, credentials policy, and review requirements.

## Harness Rules

- Put the map in `AGENTS.md`; put detailed guidance in the relevant docs file.
- Treat `docs/` as the repository-local system of record for agent-readable knowledge.
- Add indexes for directories that will grow.
- Generate or refresh `docs/generated/` files from source systems when possible.
- Add checks for freshness, cross-links, ownership, and stale docs when the repository becomes large enough.
- If a project does not need one of these files, the harness should state why it is omitted or adapted.
