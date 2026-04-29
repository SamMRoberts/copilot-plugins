# Harness Specification Template

Use this template when drafting a concrete harness.

## Harness Purpose

`[One sentence describing the coding workflow, target repository, and agent behavior the harness governs.]`

## Supported Work

- `[Task class 1]`
- `[Task class 2]`
- `[Task class 3]`

## Out Of Scope

- `[Work the agent must reject, defer, or escalate]`
- `[Destructive or high-risk operation requiring approval]`

## Required Context

Before planning or editing, the agent must inspect:

- `[Repo guidance file]`
- `[Package or project manifest]`
- `[Relevant implementation files]`
- `[Relevant tests or fixtures]`
- `[CI, schema, or workflow file]`

The agent must summarize constraints that affect implementation.

## Knowledge System

Agent entry point:

- `[Short map file, usually AGENTS.md]`

Repository-local sources of truth:

- `[docs/index.md or equivalent]`
- `[architecture or design docs]`
- `[active and completed plans]`
- `[generated references such as schemas or API docs]`

Freshness and discoverability checks:

- `[cross-link, ownership, freshness, or doc-gardening check]`

External context policy:

- `[What must be moved into the repo before agents can rely on it]`

## Operating Phases

### Intake

Entry criteria:

- User request is understood.
- Scope and likely touched areas are identified.

Exit criteria:

- Assumptions and blockers are stated.
- Questions are asked only when the answer materially changes the work.

### Discovery

Entry criteria:

- Task scope is clear enough to inspect the repository.

Exit criteria:

- Relevant files and patterns have been read.
- Existing user changes have been identified when they overlap the work.

### Plan

Entry criteria:

- The agent has enough repository context.

Exit criteria:

- Files to change, verification commands, and risk areas are known.

### Implementation

Entry criteria:

- Plan is sufficient for scoped edits.

Exit criteria:

- Edits are complete.
- No unrelated changes were made.

### Verification

Entry criteria:

- Implementation is complete.

Required gates:

- `[Command or manual check]`
- `[Command or manual check]`

Exit criteria:

- Required checks pass, or failures are explained with next action.

### Handoff

Entry criteria:

- Verification evidence has been collected or skipped with rationale.

Exit criteria:

- User receives concise summary, changed files, validation results, residual risk, and follow-up work.

## Boundaries

Edit boundaries:

- Allowed: `[paths]`
- Disallowed: `[paths]`

Command boundaries:

- Allowed without approval: `[commands]`
- Requires approval: `[commands or command classes]`

Git boundaries:

- `[branch, staging, commit, push, or PR rules]`

Dependency and network boundaries:

- `[install, download, registry, or network access rules]`

Secrets boundaries:

- `[credential and secret handling rules]`

## Agent Legibility

Runtime inspection:

- `[local startup command or environment]`
- `[worktree, sandbox, or disposable environment rule]`

UI and product evidence:

- `[DOM snapshot, screenshot, video, navigation, or manual check]`

Observability:

- `[logs, metrics, traces, query tools, dashboards, or artifact paths]`

Standard tools:

- `[CLI tools and scripts agents should use directly]`

## Mechanical Enforcement

Hard invariants:

- `[architecture, dependency, schema, logging, naming, file-size, security, or quality rule]`

Enforcement mechanism:

- `[script, test, linter, hook, schema, CI job, or MCP tool]`

Remediation guidance:

- `[What the check tells the agent to do when it fails]`

Flexible areas:

- `[Where agents have implementation freedom inside boundaries]`

## Verification Gates

Fast checks:

- `[command]`

Full checks:

- `[command]`

Manual checks:

- `[steps or screenshots required]`

Skipped-check policy:

- The agent must state the skipped check, reason, and residual risk.

## Evidence Requirements

The agent must capture:

- Commands run and pass/fail status.
- Important output lines or artifact paths.
- Screenshots, logs, or reports when relevant.
- Known gaps.

## Handoff Format

Use this structure:

```markdown
Changed [short summary].

Files:
- path/to/file

Verification:
- `command`: passed
- `command`: not run because [reason]

Risk:
- [residual risk or "No known residual risk."]
```

## Automation Plan

- Guidance files: `[AGENTS.md, skill, workflow doc]`
- Scripts: `[validation or reporting scripts]`
- Hooks: `[lifecycle hook points]`
- MCP: `[tools or persistent state]`
- Companion skills: `[phase-specific skills]`

## Feedback Loops

Failure capture:

- `[How failed runs, bugs, or review comments become durable repo updates]`

Quality maintenance:

- `[stale-doc scan, quality score, drift check, tech-debt tracker, or cleanup cadence]`

Golden principles:

- `[Opinionated mechanical rules that preserve future agent legibility]`

## Section Validation

Validation directory:

- `[.harness-validation or chosen path]`

Required section files:

- `harness_purpose.<state>.md`
- `supported_work.<state>.md`
- `out_of_scope.<state>.md`
- `required_context.<state>.md`
- `knowledge_system.<state>.md`
- `operating_phases.<state>.md`
- `boundaries.<state>.md`
- `agent_legibility.<state>.md`
- `mechanical_enforcement.<state>.md`
- `verification_gates.<state>.md`
- `evidence_requirements.<state>.md`
- `handoff_format.<state>.md`
- `automation_plan.<state>.md`
- `feedback_loops.<state>.md`
- `open_questions.<state>.md`

Status command:

```bash
python3 plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

Completion rule:

- Continue refining until each section has exactly one `complete` file.
