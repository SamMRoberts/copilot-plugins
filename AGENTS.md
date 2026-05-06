# Agent Instructions

This repository contains plugins, agents, prompts, hooks, and skills for agentic coding assistants. Treat these files as executable agent guidance: wording, metadata, and boundaries affect when agents discover capabilities and how they behave.

## Repository Map

- `README.md` is the short repository overview.
- Top-level plugin folders such as `persona-switcher/`, `software-engineering-workflow/`, and `Work Item Management/` contain distributable plugin content.
- Plugin manifests are usually `plugin.json`; keep paths in manifests relative to the plugin folder.
- Agent definitions live in `agents/*.agent.md`.
- Skills live in `skills/<skill-name>/SKILL.md`, with optional `references/`, `scripts/`, `templates/`, or `evals/` folders beside them.
- Prompt definitions live in `prompts/*.prompt.md`.
- Hook definitions and hook scripts live in `hooks.json` and `scripts/`.
- Schema or routing files, such as `workflow-routes.json` and `*.schema.json`, are source-of-truth data files and should stay machine-readable.

## Editing Principles

- Keep plugin content portable. Avoid absolute local paths, user-specific machine details, and assumptions about this checkout location.
- Preserve existing folder names and manifest contracts unless the task explicitly changes the plugin shape.
- Keep changes scoped to the requested plugin, skill, agent, or prompt. Do not refactor unrelated plugin content while editing guidance.
- Prefer explicit trigger language in skills and agents. State when to use the capability, what inputs it expects, and where its responsibility ends.
- Keep orchestration guidance narrow. Orchestrator skills may route, compare, and synthesize, but specialist work should stay in the specialist skill or agent.
- Treat descriptions and argument hints as discovery-critical metadata. Update them when behavior, scope, or required inputs change.
- Keep generated guidance concise and operational. Avoid broad philosophy unless it directly changes agent behavior.
- Use ASCII in new files unless an existing file in the same area already uses non-ASCII for a clear purpose.

## Skill Guidance

- Every `SKILL.md` should start with valid front matter containing at least `name` and `description` when the local pattern does so.
- The `description` must be strong enough for an agent to decide whether to load the skill from only the skill list.
- Put detailed examples, rubrics, and long templates in `references/` files and link to them from `SKILL.md` instead of overloading the skill body.
- Keep sub-skill relationships explicit in plugin manifests and in the orchestrating skill's procedure.
- When adding or changing eval fixtures, keep them close to the skill under `evals/` and make negative cases cover likely false triggers.

## Agent And Prompt Guidance

- Agent files should describe role, inputs, process, and output shape concretely.
- If an agent depends on another agent, skill, route table, or reference file, name that dependency with a relative path when practical.
- Prompt files should normalize user inputs into the same contracts expected by the related agent or skill.
- Do not duplicate large instructions across agents and skills when a shared reference file would be clearer.

## Plugin Manifests

- For simple plugin manifests, keep `agents`, `skills`, `hooks`, and `mcpServers` paths aligned with the actual directory names.
- For richer manifests, keep `name`, `description`, `argumentHint`, `userInvocable`, `skillPath`, and `subSkills` accurate after edits.
- Validate JSON after any manifest, route, hook, or schema edit.

## Verification

- For Markdown-only guidance changes, review the changed files for broken relative paths, stale names, and accidental scope expansion.
- For JSON changes, run a parser or formatter check such as `python3 -m json.tool <file>` or an equivalent project-local validation command.
- For hook script changes, run the script directly with representative input before relying on plugin runtime behavior.
- For skills with evals, update or run the relevant evals when the trigger behavior or output contract changes.
- Before finishing, inspect `git diff --check` and the relevant file diff.

## Collaboration Boundaries

- Do not overwrite user changes. If the worktree is dirty, understand whether the dirty files overlap your task before editing.
- Do not delete or rename plugin assets unless the user requested that structural change.
- When creating new plugin content, include enough README or inline guidance that another agent can discover the capability and use it without hidden context.
