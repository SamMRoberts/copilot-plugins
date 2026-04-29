# Coding Harness Walkthrough

Use this walkthrough when the user wants help creating a detailed harness but has not supplied all required details.

## Interview Pattern

Ask no more than three questions at a time. Prefer questions that change the resulting harness. If a reasonable default exists, state the assumption and keep moving.

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
