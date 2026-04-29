# Agentic Coding Harness

This plugin helps agents design a detailed, repository-specific harness for agentic coding work.

A coding harness is the operating contract around an agent: what it must inspect before changing code, which phases it should follow, what it may or may not edit, how it verifies work, and what evidence it must hand back to the user.

This plugin is grounded in agent-first harness engineering: keep human intent explicit, make repository knowledge the system of record, give agents a map instead of a giant manual, expose runtime evidence to agents, encode hard rules mechanically, and feed failures back into durable guidance or tooling.

## User Experience

The plugin exposes three skills:

- `create-agentic-coding-harness`: walks the user through a concrete harness design rather than returning a generic checklist.
- `review-agentic-coding-harness`: evaluates a generated harness section by section and writes `<section_name>.<state>.md` files.
- `refine-agentic-coding-harness`: uses those section-state files to regenerate, improve, or skip sections until the harness is complete.

The creation skill is interview-first:

- **Guided interview**: the default first-pass flow. It asks the user about goals, in scope, out of scope, context, boundaries, verification, and handoff before drafting.
- **Draft directly**: only when the user has already supplied all required answers or explicitly asks to skip the interview.

The skill produces a harness specification that can become an `AGENTS.md`, plugin skill, workflow document, hook plan, or script-backed validation flow.

After drafting, the skill can run a section-by-section validation loop. Each harness section gets its own markdown file named `<section_name>.<state>.md`, where `state` is `complete`, `needs_update`, or `failed`. The status script selects the next section to regenerate, improve, or skip until every section is complete.

## Harness Areas

- Purpose and target workflow.
- Repository context and required discovery.
- Repository knowledge system and agent entry-point map.
- Agent operating modes and phase gates.
- Tool, file, and permission boundaries.
- Agent legibility for runtime state, UI evidence, logs, metrics, traces, and generated artifacts.
- Mechanical enforcement for architecture, quality, safety, and taste invariants.
- Verification commands, evidence, and fallback behavior.
- Handoff format and quality bar.
- Optional automation through hooks, scripts, MCP servers, or companion skills.
- Feedback loops for failures, review comments, drift, and stale docs.
- Section-level validation and refinement.

## Plugin Shape

- `.codex-plugin/plugin.json` defines plugin metadata and points to the skill directory.
- `skills/create-agentic-coding-harness/SKILL.md` contains the main workflow.
- `skills/review-agentic-coding-harness/SKILL.md` contains the section review workflow.
- `skills/refine-agentic-coding-harness/SKILL.md` contains the iterative refinement workflow.
- `skills/create-agentic-coding-harness/references/` contains the walkthrough, output template, and examples.
- `scripts/harness_section_status.py` reports the next section-level validation action.
- `hooks/` and `assets/` are reserved for future enforcement and interface assets.
- `.mcp.json` is present as a placeholder for future MCP server wiring.
