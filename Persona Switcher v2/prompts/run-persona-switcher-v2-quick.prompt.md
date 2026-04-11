---
name: run-persona-switcher-v2-quick
description: "Run Persona Switcher v2 in quick mode with engineering-core profiles and speed-first comparison defaults."
argument-hint: "Provide task and optional constraints; quick mode defaults to engineering-core and speed-first unless you override them."
agent: "run-task-with-personas"
---
Run Persona Switcher v2 in quick mode for faster iteration.

## Default Quick Settings
- Preset id: `engineering-core`
- Comparison goal: `speed-first`

## Inputs
- Task statement
- Constraints (optional)
- Success metrics (optional)
- Optional overrides:
  - Preset id
  - Profile ids
  - Model overrides by profile id
  - Comparison goal

## Behavior
1. Normalize one canonical task statement.
2. Use `engineering-core` and `speed-first` by default.
3. Apply caller overrides when provided.
4. Run one isolated persona proposal per selected profile in parallel.
5. Return execution matrix, per-route outputs, and synthesis.

## Output Requirements
Use the exact output structure produced by `run-task-with-personas`.
