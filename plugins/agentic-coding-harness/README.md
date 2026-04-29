# Agentic Coding Harness

This plugin helps agents design a detailed, repository-specific harness for agentic coding work.

A coding harness is the operating contract around an agent: what it must inspect before changing code, which phases it should follow, what it may or may not edit, how it verifies work, and what evidence it must hand back to the user.

## User Experience

The primary skill, `create-agentic-coding-harness`, walks the user through a concrete harness design rather than returning a generic checklist. It supports two modes:

- **Guided interview**: use when the user has a goal but has not specified enough repo details.
- **Draft directly**: use when the user provides repository context, workflow boundaries, and validation expectations.

The skill produces a harness specification that can become an `AGENTS.md`, plugin skill, workflow document, hook plan, or script-backed validation flow.

After drafting, the skill can run a section-by-section validation loop. Each harness section gets its own markdown file named `<section_name>.<state>.md`, where `state` is `complete`, `needs_update`, or `failed`. The status script selects the next section to regenerate, improve, or skip until every section is complete.

## Harness Areas

- Purpose and target workflow.
- Repository context and required discovery.
- Agent operating modes and phase gates.
- Tool, file, and permission boundaries.
- Verification commands, evidence, and fallback behavior.
- Handoff format and quality bar.
- Optional automation through hooks, scripts, MCP servers, or companion skills.
- Section-level validation and refinement.

## Plugin Shape

- `.codex-plugin/plugin.json` defines plugin metadata and points to the skill directory.
- `skills/create-agentic-coding-harness/SKILL.md` contains the main workflow.
- `skills/create-agentic-coding-harness/references/` contains the walkthrough, output template, and examples.
- `scripts/harness_section_status.py` reports the next section-level validation action.
- `hooks/` and `assets/` are reserved for future enforcement and interface assets.
- `.mcp.json` is present as a placeholder for future MCP server wiring.
