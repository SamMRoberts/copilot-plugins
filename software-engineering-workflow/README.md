# Software Engineering Workflow

Software Engineering Workflow is a Copilot plugin for structured software work. It provides a standalone entry agent plus narrow phase agents that separate intake, resumption, discovery, requirements, planning, review, documentation, implementation, and verification.

Start with `software-workflow-entry` for every request. The entry agent decides whether the prompt is resumed work, new work, or ambiguous work that needs a short clarification.

## Workflow

For resumed work, the entry agent routes through `work-resumption` to reconstruct the current state and offer a continuation point. The user can continue with any phase agent:

- `context-discovery`
- `requirements-synthesis`
- `solution-planning`
- `plan-review`
- `documentation`
- `implementation`
- `verification`

For new work, the entry agent hands off to `software-workflow-orchestrator`. The orchestrator owns the user conversation and moves through these phases:

1. Information gathering with `context-discovery`
2. Requirements and acceptance criteria with `requirements-synthesis`
3. Implementation planning with `solution-planning`
4. Plan critique with `plan-review`
5. Documentation preparation with `documentation`
6. Scoped code changes with `implementation`
7. Validation and completion assessment with `verification`

## Subagent Policy

Use subagents when they improve focus or speed. Run subagents in parallel only for independent read-only work, such as inspecting separate areas of a codebase, comparing documentation, reviewing a plan, or checking test coverage assumptions. Do not parallelize file edits, commits, migrations, dependency changes, or decisions that must be sequenced.

The orchestrator remains the user-facing owner for new work. Phase agents return findings, plans, questions, or completion signals to the orchestrator unless the user explicitly resumes at that phase.

## Agent Boundaries

Each agent owns a narrow part of the software engineering workflow:

- `software-workflow-entry` classifies and routes work.
- `work-resumption` reconstructs current state and recommends a continuation point.
- `software-workflow-orchestrator` coordinates new work end to end.
- `context-discovery` gathers facts without editing files.
- `requirements-synthesis` turns facts into scoped requirements.
- `solution-planning` creates the implementation approach.
- `plan-review` finds risks before implementation.
- `documentation` prepares and updates docs.
- `implementation` performs scoped code changes.
- `verification` validates behavior and decides whether the work is complete.
