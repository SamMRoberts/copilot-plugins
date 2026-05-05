# Harness Engineering Notes

Source article: https://openai.com/index/harness-engineering/

Use these notes as design rationale when applying this skill.

## Core ideas

- Humans steer; agents execute.
- The repository should be the system of record for agent-visible knowledge.
- `AGENTS.md` should be a short routing map, not a giant manual.
- Durable knowledge belongs under `docs/` so it can be indexed, cross-linked, verified, and maintained.
- Agents need legible architecture, product specs, validation commands, logs, metrics, and app workflows.
- Documentation alone is insufficient; important architectural and quality invariants should be enforced mechanically.
- Strict boundaries and predictable structure help agents move fast without codebase decay.
- When the agent fails, treat it as a signal that documentation, tools, tests, or guardrails are missing.
- Plans should be first-class artifacts, versioned in the repository.
- Recurring doc gardening and technical-debt cleanup prevent drift.

## Harness translation

This skill implements those ideas as:

- a compact `AGENTS.md` table of contents;
- a structured `docs/` knowledge base;
- explicit harness scope and out-of-scope rules;
- active and completed execution plans;
- architecture, tooling, quality, security, reliability, and observability docs;
- a non-negotiable scope gate before code edits;
- templates that promote missing rules into docs or future mechanical checks.
