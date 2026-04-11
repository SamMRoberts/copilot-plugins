---
name: run-persona-switcher-quick
description: "Run Persona Switcher in quick mode with focused auto-selection, speed-first comparison, and concise output."
argument-hint: "Provide task and optional constraints; quick mode defaults to preset `auto`, comparison goal `speed-first`, and response depth `brief` unless you override them."
agent: "run-task-with-personas"
---
Run Persona Switcher in quick mode for faster iteration.

## Default Quick Settings
- Preset id: `auto`
- Comparison goal: `speed-first`
- Response depth: `brief`

## Inputs
- Task statement
- Decision to make (optional)
- Constraints (optional)
- Success metrics (optional)
- Optional overrides:
  - Preset id
  - Profile ids
  - Model overrides by profile id
  - Comparison goal
  - Response depth

## Behavior
1. Normalize one canonical task statement.
2. Use the default quick settings unless the caller overrides them.
3. Resolve the smallest credible persona set for the task.
4. Run one isolated persona proposal per selected profile in parallel.
5. Return a concise decision snapshot, execution matrix, per-route outputs, and synthesis.

## Output Requirements
Use the exact output structure produced by `run-task-with-personas`.
