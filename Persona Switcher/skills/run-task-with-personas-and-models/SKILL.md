---
name: run-task-with-personas-and-models
description: "Run one specified task through predefined persona and model routes, then synthesize the results. Use for multi-persona comparison, model-aware task review, or selecting a recommended path from parallel proposals."
argument-hint: "Provide the task, optional preset or persona subset, optional model overrides, constraints, and the decision you want from the comparison."
user-invocable: true
---

# Run Task With Personas And Models

## What This Skill Produces

This skill runs the same task against a curated set of predefined persona and model routes. It produces:

1. A frozen canonical task statement used for every run.
2. A resolved execution matrix showing persona, final model, and runner agent.
3. One isolated output per selected persona and model route.
4. A cross-route synthesis with agreements, disagreements, and a recommended path.

## Source Of Truth

Predefined persona and model routes are stored in [Predefined Persona-Model Profiles](./references/personas/predefined-persona-models.json).

That manifest defines:

- Available persona profiles.
- Default model per persona.
- Runner agent per model.
- Supported model override routes.
- Ready-made profile selection presets.

## Default Persona Set

The predefined defaults are:

- Software Engineer (Junior) -> GPT-5 mini (copilot)
- Software Engineer (Mid-level) -> GPT-5.2 (copilot)
- Software Engineer (Senior) -> GPT-5.4 (copilot)
- Site Reliability Engineer (Junior) -> Claude Haiku 4.5 (copilot)
- Site Reliability Engineer (Mid-level) -> GPT-4.1 (copilot)
- Site Reliability Engineer (Senior) -> Gemini 3.1 Pro (Preview) (copilot)
- Engineering Manager -> Gemini 2.5 Pro (copilot)
- Program Manager -> Claude Sonnet 4.5 (copilot)
- Product Manager -> Claude Sonnet 4.6 (copilot)

## When To Use

- You want the same task evaluated by multiple predefined personas.
- You want model diversity without redefining persona instructions each time.
- You need a side-by-side comparison before choosing an implementation path.
- You want a preset selection such as engineering-only, delivery-triad, or reliability-focus.

## Required Inputs

- Task statement.
- Optional constraints.
- Optional success metrics.
- Optional preset id or explicit persona subset.
- Optional model overrides by persona.
- Optional comparison goal such as risk-first, speed-first, or strongest recommendation.

If required context is missing, ask only the minimum clarification questions needed to avoid scope drift. If the user does not answer, proceed with explicit assumptions.

## Selection Rules

- Default selection is the `full-team` preset from the manifest.
- If a preset is provided, load exactly that preset's profiles unless the user also supplies an explicit subset.
- If both preset and explicit subset are supplied, the explicit subset wins.
- If a requested persona is not in the manifest, do not invent a new profile; report it as unsupported.

## Routing Rules

Resolve each selected persona route in this order:

1. Explicit model override supplied by the user, if the model exists in `supportedModelRoutes`.
2. The persona's `defaultModel` and `runnerAgent` from the manifest.
3. Generic fallback route:
   - Model: unspecified
  - Runner agent: `persona-proposal-runner`

Do not change the canonical task text across routes.

## Execution Contract

- Runtime handoff is mandatory: always execute through `run-task-with-personas.agent.md` (agent name: `run-task-with-personas`).
- This skill is guidance and output-shape policy; it is not the runtime controller.
- Run one isolated subagent call per selected persona.
- Keep each invocation stateless and independent.
- Pass the same task, constraints, and success metrics to every route.
- Apply persona-specific framing only through the selected profile.
- Continue if one route fails; synthesize successful outputs and list missing routes.

Each routed invocation should include:

- Canonical task statement.
- Constraints.
- Success metrics.
- Persona profile name, role, experience, and personality.
- Resolved model and runner agent.
- Comparison goal if provided.

## Procedure

1. Normalize the task into one canonical statement.
2. Read the predefined manifest and select profiles.
3. Build one invocation payload for the orchestrator containing task, constraints, success metrics, preset/subset, overrides, and comparison goal.
4. Delegate execution to `run-task-with-personas`.
5. Let `run-task-with-personas` resolve model overrides and final runner agents.
6. Let `run-task-with-personas` invoke selected persona routes in parallel and return normalized outputs.
7. Compare proposals across risk, speed, maintainability, and delivery confidence.
8. Recommend a path that fits the user's stated comparison goal.

## Decision Rules

- If the user does not specify a comparison goal, default to risk-first.
- If multiple routes converge on the same recommendation, highlight the consensus instead of repeating identical detail.
- If outputs differ sharply, explain the conflict in terms of role incentives, not just wording differences.
- If a model override conflicts with supported routes, ignore the override and note it under assumptions.
- If more than half of the selected routes fail, stop short of a strong recommendation and report the run as incomplete.

## Output Format

Use this structure:

### Task
- Canonical task text:
- Constraints:
- Success metrics:
- Comparison goal:
- Personas selected:

### Execution Matrix
- Persona name | Role | Default model | Final model | Runner agent | Route reason

### Per-Route Outputs
- Persona name:
  - Model:
  - Runner agent:
  - Approach:
  - Risks:
  - Tradeoffs:
  - First steps:
  - Definition of done:

### Synthesis
- Areas of agreement:
- Areas of disagreement:
- Recommended path:
- Strongest speed-first option:
- Strongest risk-first option:
- Rationale:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

## Authoring Guidance

- Keep the task fixed once normalized.
- Use the manifest as the only source of truth for predefined routes.
- Do not fabricate model support or runner agent names.
- Prefer explicit execution matrices over prose-only summaries.
- Keep synthesis grounded in route differences that matter to the user's decision.
- Do not bypass `run-task-with-personas`; all runtime execution must be handed off to that agent.