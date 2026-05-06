# Agentic Coding Harness

This Codex plugin initializes, reviews, refines, and validates repository-local agentic coding harnesses.

## Install locally as a plugin

Copy this folder to:

```text
<repo>/.agents/plugins/agentic-coding-harness/
```

Then invoke it from Codex by asking to initialize, review, refine, or validate the agentic coding harness.

## Initialize a repository harness

From the repository root:

```bash
python .agents/plugins/agentic-coding-harness/scripts/init_harness.py
```

For defaults without prompts:

```bash
python .agents/plugins/agentic-coding-harness/scripts/init_harness.py --non-interactive
```

To use a JSON answers file:

```bash
python .agents/plugins/agentic-coding-harness/scripts/init_harness.py --answers harness-answers.json
```

## Validate a repository harness

From the repository root:

```bash
python .agents/plugins/agentic-coding-harness/scripts/validate_harness.py
```

## What it creates

- `AGENTS.md`, kept close to 100 lines and used as a routing table.
- `docs/`, containing harness scope, design docs, execution plans, app specs, references, architecture, tooling, quality, security, reliability, observability, and review docs.
- `.harness-validation/`, when reviewing or refining a harness section by section.

## Guardrail behavior

Before code changes, agents must classify the task against the harness. If a requested change conflicts with the harness, is explicitly out of scope, or is not included in scope, the agent must not edit code and must ask whether to update the harness, stop, or create a new in-scope plan.
