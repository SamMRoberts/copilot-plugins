# Persona Switcher

Persona Switcher is a task-centric bundle for running the same request through curated persona and model routes, then returning a recommendation instead of an unsorted pile of opinions.

## Required VS Code Setting

To enable nested subagent invocation, your VS Code `settings.json` must include:

```json
{
	"chat.subagents.allowInvocationsFromSubagents": true
}
```

## Included

- [run-task-with-personas-and-models](./skills/run-task-with-personas-and-models/SKILL.md)
- [run-task-with-personas](./agents/run-task-with-personas.agent.md)
- [run-persona-switcher](./prompts/run-persona-switcher.prompt.md)
- [run-persona-switcher-quick](./prompts/run-persona-switcher-quick.prompt.md)

## What Changed In This Version

- Focused routing is now the default experience.
- The orchestrator is encouraged to choose the smallest credible preset instead of always blasting the full team.
- Outputs are shaped around a decision snapshot, per-route recommendations, and a clearer synthesis.
- Quick mode now defaults to concise output for faster iteration.
- Skill-aware runs now support named skills plus local skill references, with shared guidance resolved once and reused across routes.

## How It Works

1. Normalize one canonical task statement.
2. Infer the decision that needs to be made.
3. Select explicit personas, a named preset, or a focused preset automatically.
4. Resolve optional skill names or skill references into one shared guidance packet.
5. Resolve each persona to a default model and runner agent.
6. Apply optional model overrides when the route is supported.
7. Run the selected routes in parallel.
8. Return a decision snapshot, per-route outputs, and a synthesis.

## Default Preset Strategy

If you do not specify personas or a preset, Persona Switcher should choose a focused preset automatically:

- `engineering-core` for implementation and bug-fix work
- `technical-design` for architecture, refactors, and migrations
- `incident-response` for reliability and operational work
- `launch-readiness` for rollout and delivery coordination
- `product-discovery` for prioritization and value tradeoffs
- `full-team` only when broad coverage is clearly useful

## Available Presets

The manifest currently includes:

- `full-team`
- `engineering-core`
- `reliability-focus`
- `delivery-triad`
- `technical-design`
- `incident-response`
- `launch-readiness`
- `product-discovery`

## Prompts

### `run-persona-switcher`

Use this when you want the standard Persona Switcher flow with focused auto-selection, standard detail, and a recommendation-driven synthesis.

You can also provide optional skill names and/or a skill reference so every persona evaluates the task against the same extra guidance.

Example inputs for [`run-persona-switcher.prompt.md`](./prompts/run-persona-switcher.prompt.md):

#### Example 1: Focused implementation review

```md
Task statement: Fix a flaky GitHub Actions workflow that intermittently fails during npm install.
Decision to make: Choose the safest fix that reduces retries without slowing the happy path too much.
Constraints:
- Keep the existing workflow structure if possible.
- Avoid adding new third-party actions unless clearly justified.
Success metrics:
- Fewer transient install failures.
- Minimal added execution time.
Comparison goal: risk-first
Response depth: standard
```

#### Example 2: Explicit persona and model routing

```md
Task statement: Propose a migration plan from ad-hoc REST polling to webhooks for plugin sync events.
Decision to make: Pick the best rollout approach for engineering effort versus operational risk.
Profile ids:
- staff-engineer
- sre
- product-manager
Model overrides by profile id:
- staff-engineer: gpt-5-4
- sre: claude-sonnet-4-6
Constraints:
- Preserve backwards compatibility for existing plugin consumers during rollout.
- Include observability checkpoints.
Comparison goal: risk-first
Response depth: deep
```

#### Example 3: Skill-aware comparison with shared context

```md
Task statement: Design a safer release checklist for Persona Switcher updates that change agent contracts.
Decision to make: Decide whether to gate releases on a manual review step or automated validation only.
Skill names:
- customizing-copilot-cloud-agents-environment
Skill objective: Reuse any relevant agent-environment guidance while comparing release options.
Skill execution mode: advisory
Constraints:
- Keep the checklist lightweight enough for small releases.
- Call out failure modes caused by unsupported agent configuration.
Success metrics:
- Fewer release regressions.
- Clearer rollback criteria.
Comparison goal: risk-first
Response depth: standard
```

#### Example 4: Local skill-reference input

```md
Task statement: Compare two approaches for documenting Persona Switcher presets in the repo README.
Decision to make: Choose whether to organize the docs by preset type or by user workflow.
Skill reference path: Persona Switcher/skills/run-task-with-personas-and-models/SKILL.md
Skill objective: Reuse the orchestrator contract and output shape while evaluating the doc structure.
Skill execution mode: required
Constraints:
- Keep the README approachable for first-time users.
- Do not duplicate prompt details unnecessarily.
Comparison goal: risk-first
Response depth: standard
```

### `run-persona-switcher-quick`

Use this when you want a faster pass. Quick mode defaults to:

- preset id: `auto`
- comparison goal: `speed-first`
- response depth: `brief`

Quick mode also accepts optional skill names and/or a skill reference when you want faster skill-aware comparisons.

## Output Shape

Persona Switcher now aims to return:

1. A **Decision Snapshot** with the best route, main risk, fallback option, and next move.
2. A **Task** section showing the frozen task, decision, and chosen personas.
3. The shared skill context that was reused across routes when skills were supplied.
4. An **Execution Matrix** showing which persona used which model and runner.
5. **Per-Route Outputs** with recommendations, risks, tradeoffs, first steps, and skill interactions.
6. A **Synthesis** that explains the winner, alternatives, and missing coverage.

## Reference Data

The predefined persona and model routes live in [predefined-persona-models.json](./skills/run-task-with-personas-and-models/references/personas/predefined-persona-models.json).

## Agent Topology

- Orchestrator: [run-task-with-personas](./agents/run-task-with-personas.agent.md)
- Generic worker fallback: [persona-proposal-runner](./agents/persona-proposal-runner.agent.md)
- Model-pinned workers: [agents](./agents)
