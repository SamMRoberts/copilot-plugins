---
name: create-agentic-coding-harness
description: "Use when a user wants to design, create, refine, validate, or document a detailed coding harness for agentic coding work. Covers repository discovery, setup checks, agent operating phases, tool and file boundaries, verification gates, evidence capture, handoff artifacts, section-by-section completeness evaluation, hooks, scripts, MCP support, and AGENTS.md-style guidance. Do not use for ordinary feature implementation unless the task is to build or improve the harness itself."
argument-hint: "Describe the target repository, agent workflow, coding tasks to support, boundaries, verification commands, and desired handoff artifacts."
---

# Create Agentic Coding Harness

Use this skill to help a user create a detailed, specific harness for agentic coding agents.

The harness is the operating contract around coding work: what the agent inspects, how it plans, what it may change, how it validates changes, and what it reports back.

## Mode Selection

- If the user asks for a walkthrough, interview, or help shaping the harness, use the guided walkthrough in `references/walkthrough.md`.
- If the user provides enough context to draft the harness, produce a concrete specification using `references/harness-spec-template.md`.
- If the user asks to validate, refine, iterate, or prove completeness, use `references/section-refinement.md` and the script `../../scripts/harness_section_status.py`.
- If the user asks what good output looks like, load `references/examples.md`.

## Required Inputs

Collect or infer:

- Repository type, languages, frameworks, package managers, and test runners.
- Coding tasks the harness must support.
- Required discovery sources such as `AGENTS.md`, README files, manifests, route tables, schemas, architecture notes, or issue templates.
- File, command, branch, network, and permission boundaries.
- Planning expectations before edits.
- Verification commands, manual checks, and evidence requirements.
- Final response or handoff format.
- Durable guidance location, such as `AGENTS.md`, a plugin skill, a workflow doc, or generated scripts.

Ask at most three targeted questions when missing information would materially change the harness. Otherwise make conservative assumptions and label them.

## Walkthrough Flow

1. Define the harness mission in one sentence.
2. Identify the supported task classes and excluded work.
3. Map the repository context an agent must read before acting.
4. Define the agent phase model: intake, discovery, plan, implementation, verification, handoff, and optional memory or follow-up capture.
5. Set boundaries for tools, files, destructive commands, dependencies, network access, generated artifacts, and user approval.
6. Define verification gates with exact commands where possible.
7. Define evidence capture: command results, screenshots, logs, diffs, test artifacts, or skipped-check explanations.
8. Define the user handoff: concise summary, changed files, validation, residual risk, and next steps.
9. Recommend where the harness should live and which parts should be automated.
10. Validate the generated harness section by section when the user wants a complete harness or when the harness will become durable guidance.

## Section Validation Phase

When validating completeness, split the harness into section files under a validation directory such as `.harness-validation/`.

Each file must be named:

```text
<section_name>.<state>.md
```

Use snake_case section names. Valid states:

- `complete`: no more work is needed.
- `needs_update`: improve this section in another pass using its current content.
- `failed`: regenerate this section from scratch.

Default sections:

- `harness_purpose`
- `supported_work`
- `out_of_scope`
- `required_context`
- `operating_phases`
- `boundaries`
- `verification_gates`
- `evidence_requirements`
- `handoff_format`
- `automation_plan`
- `open_questions`

Run the status script after creating or updating section files:

```bash
python3 plugins/agentic-coding-harness/scripts/harness_section_status.py --dir .harness-validation
```

If a section is `failed`, create a new version from scratch and rename the file to the new state. If a section is `needs_update`, improve the existing content and rename the file to the new state. If a section is `complete`, skip it. Continue until the script reports all sections complete.

## Output Contract

Return a practical harness package:

- **Harness Purpose**: specific workflow and target users.
- **Supported Work**: task classes the harness covers.
- **Out Of Scope**: work the harness should reject or escalate.
- **Required Context**: files, commands, and repo signals to inspect.
- **Operating Phases**: ordered phase gates with entry and exit criteria.
- **Boundaries**: edit, tool, permission, dependency, network, and git constraints.
- **Verification Gates**: commands and evidence required before handoff.
- **Handoff Format**: final response structure or artifact template.
- **Automation Plan**: guidance-only, hooks, scripts, MCP server, companion skills, or a combination.
- **Open Questions**: only blockers that cannot be safely assumed.
- **Section Validation Files**: section-level markdown files and their final states when validation was requested.

## Quality Bar

- Make the harness concrete enough that another agent can follow it without hidden context.
- Prefer exact file paths, commands, and decision points over general advice.
- Separate required gates from optional checks.
- Make escalation and stop conditions explicit.
- Keep domain implementation guidance out of the harness unless it directly affects agent behavior.
- Do not mark a section `complete` until it is specific, internally consistent, and usable by another agent without hidden context.
