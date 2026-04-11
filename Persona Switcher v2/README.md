# Persona Switcher v2

Persona Switcher v2 is a task-centric skill bundle for running the same prompt through predefined persona and model routes, then comparing the outputs.

## Included

- [run-task-with-personas-and-models](./skills/run-task-with-personas-and-models/SKILL.md)

## How It Works

1. Normalize one task statement.
2. Select a preset or explicit persona subset.
3. Resolve each persona to a default model and runner agent.
4. Apply optional model overrides when the route is supported.
5. Run the selected routes in parallel.
6. Return per-route outputs plus a synthesis.

## Reference Data

The predefined persona and model routes live in [predefined-persona-models.json](./skills/run-task-with-personas-and-models/references/predefined-persona-models.json).

The v2 skill reuses the existing model-specific runner agents already defined in the main [Persona Switcher](../Persona%20Switcher) folder.