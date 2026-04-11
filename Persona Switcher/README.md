# Persona Switcher

Persona Switcher is a task-centric bundle for running the same request through curated persona and model routes, then returning a recommendation instead of an unsorted pile of opinions.

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

## How It Works

1. Normalize one canonical task statement.
2. Infer the decision that needs to be made.
3. Select explicit personas, a named preset, or a focused preset automatically.
4. Resolve each persona to a default model and runner agent.
5. Apply optional model overrides when the route is supported.
6. Run the selected routes in parallel.
7. Return a decision snapshot, per-route outputs, and a synthesis.

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

### `run-persona-switcher-quick`

Use this when you want a faster pass. Quick mode defaults to:

- preset id: `auto`
- comparison goal: `speed-first`
- response depth: `brief`

## Output Shape

Persona Switcher now aims to return:

1. A **Decision Snapshot** with the best route, main risk, fallback option, and next move.
2. A **Task** section showing the frozen task, decision, and chosen personas.
3. An **Execution Matrix** showing which persona used which model and runner.
4. **Per-Route Outputs** with recommendations, risks, tradeoffs, and first steps.
5. A **Synthesis** that explains the winner, alternatives, and missing coverage.

## Reference Data

The predefined persona and model routes live in [predefined-persona-models.json](./skills/run-task-with-personas-and-models/references/personas/predefined-persona-models.json).

## Agent Topology

- Orchestrator: [run-task-with-personas](./agents/run-task-with-personas.agent.md)
- Generic worker fallback: [persona-proposal-runner](./agents/persona-proposal-runner.agent.md)
- Model-pinned workers: [agents](./agents)
