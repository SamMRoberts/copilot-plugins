---
name: run-persona-switcher-v2
description: "Run Persona Switcher v2 end-to-end for a single task using predefined personas and model routes."
argument-hint: "Provide task, optional constraints, success metrics, optional preset/profile ids, optional model overrides, and comparison goal."
agent: "run-task-with-personas"
---
Run Persona Switcher v2 end-to-end using the `run-task-with-personas` orchestrator.

## Inputs
- Task statement
- Constraints (optional)
- Success metrics (optional)
- Preset id (optional)
- Profile ids (optional)
- Model overrides by profile id (optional)
- Comparison goal (optional)

## Behavior
1. Normalize and freeze one canonical task statement.
2. Resolve selected persona profiles from preset or explicit profile ids.
3. Resolve model routes using defaults plus valid overrides.
4. Run one isolated persona proposal per selected profile in parallel.
5. Return execution matrix, per-route outputs, and synthesis.

## Output Requirements
Use the exact output structure produced by `run-task-with-personas`.
