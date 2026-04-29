# Agentic Coding Harness

This plugin is a scaffold for building a reusable harness around agentic coding workflows.

The harness should help agents run coding work with explicit setup, context capture, execution boundaries, verification, and handoff artifacts. Keep this plugin focused on repeatable harness behavior rather than domain-specific implementation guidance.

## Current Shape

- `.codex-plugin/plugin.json` contains the required plugin manifest with TODO placeholders.
- `skills/` is reserved for harness planning, execution, verification, and reporting skills.
- `hooks/` and `scripts/` are reserved for runtime checks, context capture, and validation helpers.
- `assets/` is reserved for plugin icons, screenshots, and related visual assets.
- `.mcp.json` is present as a placeholder for future MCP server wiring.

## Suggested Next Steps

1. Replace manifest TODO values once the plugin scope, publisher, and distribution target are clear.
2. Decide whether this plugin should expose one orchestration skill or multiple narrower skills.
3. Define the harness contract: inputs, setup checks, execution phases, verification evidence, and final handoff format.
4. Add scripts only when they enforce a real harness behavior, such as validating required files or summarizing work state.
