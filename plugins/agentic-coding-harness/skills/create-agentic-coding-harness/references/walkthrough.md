# Coding Harness Walkthrough

Use this walkthrough for first-pass harness creation. Do not draft the harness until the required interview categories are answered or the user explicitly asks to skip the interview.

## Interview Pattern

Ask questions in short rounds. Use no more than five questions per round.

Do not silently infer goals, scope, boundaries, or validation requirements. If the user has not answered a required category, ask about it. If the user explicitly declines to answer a category, record the gap as an assumption or open question and continue.

After each answer, briefly summarize what was learned and ask the next question set. Draft only after the interview gate is satisfied.

## Interview Gate

The harness is ready to draft only when these categories are known:

- Goal and success criteria.
- Target repository or repository family.
- In-scope task classes.
- Out-of-scope task classes and stop conditions.
- Required context and discovery sources.
- Repository knowledge system and map of deeper sources of truth.
- Tool, file, command, network, dependency, permission, and git boundaries.
- Agent legibility for runtime state, logs, metrics, traces, screenshots, and other evidence.
- Mechanical enforcement for hard invariants.
- Verification gates and evidence requirements.
- Feedback loops for failures, review comments, drift, and stale docs.
- Handoff artifact format.
- Desired destination for the harness.

## Question Rounds

Use these rounds in order. Skip questions that the user has already answered.

### Round 1: Goals And Target

1. What is the main goal of this coding harness?
2. What repository, repository type, or family of repositories should it apply to?
3. What would make the harness successful in practice?
4. Who is the harness for: a general coding agent, a specific agent, a team workflow, or a plugin/skill workflow?

### Round 2: Scope

1. What kinds of coding work are in scope?
2. What kinds of work are explicitly out of scope?
3. What situations should force the agent to stop and ask before continuing?
4. Are there task classes that should be review-only rather than implementation-ready?

### Round 3: Context And Discovery

1. Which files must an agent read before planning or editing?
2. Which repo signals should the agent inspect, such as manifests, schemas, CI workflows, tests, route tables, or existing guidance?
3. Should the agent summarize discovered constraints before it starts implementation?
4. Are there domain-specific docs or decisions that must override general agent behavior?
5. Should the harness use a short `AGENTS.md` as a map to deeper docs instead of storing all guidance in one file?

### Round 4: Knowledge System And Legibility

1. What repository-local knowledge base should be the system of record, such as `docs/`, plans, product specs, architecture docs, or generated schema references?
2. Which docs need indexes, ownership, freshness checks, or cross-link validation?
3. What runtime evidence should the agent be able to inspect, such as app state, UI snapshots, logs, metrics, traces, videos, or screenshots?
4. Should the app or service run in isolated worktrees, disposable environments, or task-specific sandboxes?
5. What standard tools should agents use directly instead of asking humans to paste context?

### Round 5: Boundaries

1. Which files or directories may the agent edit?
2. Which files, commands, or operations are forbidden without explicit approval?
3. What are the dependency installation and network access rules?
4. What are the git rules for branches, staging, commits, pushes, and dirty worktrees?
5. Are there secrets, credentials, production systems, or destructive operations that need special handling?

### Round 6: Mechanical Enforcement

1. Which architecture, dependency, naming, logging, schema, file-size, or quality rules must be enforced mechanically?
2. Should enforcement live in scripts, tests, linters, hooks, schemas, CI jobs, or another mechanism?
3. What remediation instructions should enforcement errors give back to agents?
4. Which guidance should remain flexible rather than mechanically enforced?

### Round 7: Verification, Feedback, And Handoff

1. Which commands or checks are required before the agent reports completion?
2. What evidence should the agent capture, such as command output, logs, screenshots, test artifacts, or changed files?
3. How should review comments, bugs, failed runs, or repeated mistakes become durable docs, tests, scripts, hooks, or cleanup tasks?
4. Should the harness include recurring garbage collection for drift, stale docs, or inconsistent patterns?
5. What should the final handoff include?
6. Where should the harness live: `AGENTS.md`, plugin skill, workflow document, hook/script system, or another artifact?
7. Should the generated harness be reviewed and refined using section-state files?

## Step 1: Mission

Clarify what the harness is for.

Useful prompts:

- What kind of coding work should this harness govern?
- Is the harness for one repository, a family of repositories, or general agent behavior?
- Should it produce an `AGENTS.md`, plugin skill, workflow document, validation script, or all of those?

Output:

- One-sentence mission.
- Primary users.
- Target repositories or environments.

## Step 2: Supported Work

Define the work the harness should handle.

Capture:

- Feature implementation.
- Bug fixing.
- Refactors.
- Test writing.
- CI repair.
- Documentation updates.
- Release or packaging work.
- Review-only work.

Also capture explicit exclusions, such as production deploys, credentials work, destructive migrations, or broad architecture rewrites.

## Step 3: Required Discovery

Define what an agent must read before it plans or edits.

Common sources:

- `AGENTS.md`.
- `README.md`.
- Package manifests.
- Build and test config.
- Existing skills, prompts, or plugin manifests.
- Architecture docs.
- API schemas.
- Database schemas.
- CI workflows.
- Existing tests around the touched area.

Require the agent to summarize discovered constraints before implementation when the task has meaningful risk.

## Step 3A: Knowledge System

Define the repository-local system of record. Prefer a short agent entry point that links to deeper docs, plans, schemas, and references.

Capture:

- The entry-point map, usually `AGENTS.md`.
- Deeper docs and indexes.
- Active and completed plans.
- Generated references such as schema docs.
- Freshness, ownership, and cross-link checks.
- What knowledge must be moved from external systems into the repo.

## Step 4: Operating Phases

A strong harness usually has these phases:

1. Intake: restate request, scope, assumptions, and blockers.
2. Discovery: inspect repo guidance, touched areas, tests, and dependencies.
3. Plan: state files to change, verification plan, and risks.
4. Implementation: make scoped edits.
5. Verification: run required checks and inspect output.
6. Handoff: summarize changes, evidence, skipped checks, residual risk, and next steps.

For low-risk tasks, allow phases to be compressed while preserving the same gates.

## Step 5: Boundaries

Define hard rules:

- Files or directories agents may edit.
- Files or directories agents must not edit.
- Commands that require approval.
- Network or dependency installation rules.
- Git branch, commit, and push behavior.
- Handling dirty worktrees and user changes.
- Generated artifact policy.
- Secrets and credentials policy.

Make stop conditions explicit. Examples: ambiguous destructive operation, conflicting user changes, missing credentials, failing migration, or verification command that cannot run.

## Step 5A: Agent Legibility

Define how agents inspect the system while it runs.

Capture:

- Local app startup commands.
- Worktree or task isolation model.
- UI navigation, screenshots, videos, or DOM snapshots.
- Logs, metrics, traces, and query tools.
- Runtime artifacts the agent must collect before claiming success.

## Step 5B: Mechanical Enforcement

Define hard rules that should not rely on prose alone.

Capture:

- Architecture and dependency direction checks.
- Schema and boundary validation.
- Structured logging or observability rules.
- Naming conventions and file-size limits.
- Custom lint messages that tell agents how to remediate failures.
- CI or hook jobs that keep knowledge docs current.

## Step 6: Verification

Define exact checks when possible.

Capture:

- Fast validation commands.
- Full validation commands.
- Manual UI checks.
- Screenshot or artifact requirements.
- Log inspection.
- Schema validation.
- Lint, typecheck, test, build, smoke, and integration gates.

Require agents to report command names and outcomes. If a check is skipped, require a reason and residual risk.

## Step 7: Handoff

Define the final response shape.

Recommended fields:

- What changed.
- Files changed.
- Verification run.
- Verification not run and why.
- Known risks.
- Follow-up work.

The handoff should be short enough to read quickly but specific enough to audit.

## Step 7A: Feedback Loops

Define how the harness improves after agent runs.

Capture:

- How review comments become docs, tests, scripts, or hooks.
- How bugs produce reproduction steps and validation gates.
- How repeated mistakes become golden principles.
- How stale docs and drift are detected.
- Which recurring cleanup tasks should run.

## Step 8: Automation Decision

Choose the smallest durable enforcement:

- Guidance only: best for flexible human-in-the-loop workflows.
- Script: best for deterministic validation or report generation.
- Hook: best for automatically checking required behavior at lifecycle points.
- MCP server: best when the harness needs persistent state, external systems, or structured tools.
- Companion skills: best when the harness has separable phases or specialist workflows.

## Step 9: Section Validation

When the harness is intended to become durable guidance, validate it by section.

Create one markdown file per section in a validation directory, using this naming pattern:

```text
<section_name>.<state>.md
```

Use `complete`, `needs_update`, or `failed` as the state. Then run:

```bash
python3 plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

Use the script output as the next action. Regenerate failed sections, improve sections that need updates, and skip complete sections. Repeat until all sections are complete.
