---
name: run-persona-switcher
description: "Run Persona Switcher end-to-end for a single task using focused persona selection, predefined model routes, and optional skill context."
argument-hint: "Provide task, optional decision to make, constraints, success metrics, optional preset/profile ids, optional model overrides, optional skill names and/or a skill reference/objective/mode, optional comparison goal, and optional response depth."
agent: "run-task-with-personas"
---
Run Persona Switcher end-to-end using the `run-task-with-personas` orchestrator.

## Inputs
- Task statement
- Decision to make (optional)
- Constraints (optional)
- Success metrics (optional)
- Preset id (optional; `auto` allowed)
- Profile ids (optional)
- Model overrides by profile id (optional)
- Skill names (optional)
- Skill reference path (optional)
- Skill objective (optional)
- Skill execution mode (optional: `advisory` or `required`)
- Comparison goal (optional)
- Response depth (optional: `brief`, `standard`, or `deep`)

## Default Behavior
- If no preset or profile ids are provided, use focused auto-selection.
- Default response depth is `standard`.
- Default comparison goal is `risk-first`.
- If the user explicitly asks for wide coverage, prefer `full-team`.

## Behavior
1. Normalize and freeze one canonical task statement.
2. Infer the decision that needs to be made.
3. Resolve selected persona profiles from profile ids, a preset, or focused auto-selection.
4. Resolve model routes using defaults plus valid overrides.
5. If skill names or a skill reference are provided, normalize shared skill context once and pass it to each persona route with the same objective and mode.
6. Run one isolated persona proposal per selected profile in parallel.
7. Return a decision snapshot, execution matrix, per-route outputs, and synthesis.
8. Include explicit result-processing notes that explain how returned persona outputs were grouped, weighted, conflict-resolved, and selected into the final recommendation.

## Output Requirements
Use the exact output structure produced by `run-task-with-personas`.
The output must include a `Result Processing Notes` section that explains, in plain language, what the system did with multiple persona results.
