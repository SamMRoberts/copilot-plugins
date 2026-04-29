# Agent-First Harness Principles

This reference captures harness-design principles from the OpenAI harness engineering article reviewed during plugin development. Use it when creating, reviewing, or refining a coding harness.

## Core Premise

Humans steer; agents execute. The harness should help humans specify intent, define boundaries, and build feedback loops that let coding agents do reliable work with minimal hidden context.

## Harness Design Principles

### Make The Repository Legible To Agents

Anything the agent cannot inspect during a run effectively does not exist. Prefer repository-local, versioned artifacts over external chat threads, private docs, or oral context.

The harness should ask:

- What knowledge must move into the repo?
- Which docs, schemas, plans, logs, metrics, screenshots, or scripts make the system inspectable?
- What must be generated or refreshed so the agent can reason from current facts?

### Give Agents A Map, Not A Manual

Do not turn `AGENTS.md` into a giant encyclopedia. Use a short entry point that maps the agent to deeper sources of truth.

The harness should define:

- A short agent entry file, often `AGENTS.md`.
- The default structured knowledge base from `repository-docs-structure.md`, unless the user explicitly chooses another layout.
- Index files and cross-links that tell agents where to look next.
- Ownership, freshness, and verification rules for deeper docs.

### Encode Invariants Mechanically

Documentation alone does not preserve architecture or taste. Important boundaries should become scripts, linters, tests, hooks, schemas, or CI checks.

The harness should distinguish:

- Hard invariants that must be enforced mechanically.
- Soft guidance that can stay in docs.
- Local implementation freedom that agents may use inside the enforced boundaries.

### Optimize For Strict Boundaries And Predictable Structure

Agents work better when the repository has stable layers, named interfaces, limited dependency directions, and clear allowed edges.

The harness should define:

- Layering and dependency rules.
- Allowed cross-cutting interfaces.
- File and package naming conventions.
- Size, logging, schema, and boundary-validation rules.

### Make Feedback Loops First-Class

When agents fail, treat it as a missing capability, missing context, missing guardrail, or missing verification loop. Feed the fix back into the repository.

The harness should capture:

- How review comments become docs, tests, hooks, or scripts.
- How bugs produce repro steps and validation gates.
- How flaky or missing checks are repaired.
- How recurring cleanup catches drift before it compounds.

### Use Standard Tools Directly

Agents should use the same tools engineers use: local scripts, test commands, GitHub CLI, app drivers, observability queries, and repo-embedded skills.

The harness should specify:

- Exact commands agents should run.
- What output is meaningful.
- How agents gather PR feedback and respond.
- Which tools require user approval.

### Make Runtime State Inspectable

For applications, code alone is not enough. Agents need access to running app state, UI snapshots, logs, metrics, traces, videos, and reproducible environments.

The harness should ask:

- Can the app run per worktree or per task?
- How does the agent reproduce reported failures?
- How does it validate UI or runtime behavior?
- Which logs, metrics, traces, or artifacts should it inspect?

### Design For Continuous Garbage Collection

Agent-generated systems accumulate drift by copying existing patterns. The harness should define recurring cleanup and quality checks.

The harness should include:

- Golden principles.
- Quality score or debt tracking.
- Stale-doc detection.
- Scheduled cleanup tasks.
- Small targeted refactoring loops.

## Harness Review Questions

Use these questions when evaluating a generated harness:

- Does the harness turn external knowledge into repository-local artifacts?
- Is the main agent entry point a concise map to deeper docs?
- Are hard rules enforceable by scripts, tests, hooks, schemas, or CI?
- Does the harness make the application, logs, metrics, and test results legible to agents?
- Does it describe what agents should do when a run fails?
- Does it include a feedback loop for converting failures and review comments into durable guidance?
- Does it preserve human judgment for the right decisions while letting agents execute repeatable work?
