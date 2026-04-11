---
name: run-task-with-personas-and-models
description: "Run one specified task through predefined persona and model routes, then synthesize the results. Use for multi-persona comparison, model-aware task review, or selecting a recommended path from parallel proposals."
argument-hint: "Provide the task, optional decision to make, optional preset or persona subset, optional model overrides, constraints, success metrics, and the decision you want from the comparison."
user-invocable: true
---

# Run Task With Personas And Models

## What This Skill Produces

This skill runs the same task against a curated set of predefined persona and model routes. It produces a decision-ready packet with:

1. A frozen canonical task statement used for every run.
2. A focused execution matrix showing persona, final model, and runner agent.
3. One isolated output per selected persona and model route.
4. A synthesis that names the best path, the strongest alternative, and the tradeoff that separates them.

## Source Of Truth

Predefined persona and model routes are stored in [Predefined Persona-Model Profiles](./references/personas/predefined-persona-models.json).

That manifest defines:

- Available persona profiles.
- Default model per persona.
- Runner agent per model.
- Supported model override routes.
- Ready-made profile selection presets.

## When To Use

Use this skill when:

- You want the same task evaluated by multiple predefined personas.
- You want model diversity without redefining persona instructions each time.
- You need a side-by-side comparison before choosing an implementation path.
- You want the output to end with a clear recommendation instead of only listing opinions.

## Default Experience

Prefer focused reviews over a full-team blast unless the user explicitly asks for broad coverage.

If the user does not specify `profileIds` or a preset, resolve a focused preset automatically:

- Implementation, bug fix, test work, or code generation -> `engineering-core`
- Technical design, migration, refactor, or platform change -> `technical-design`
- Incident response, resilience, rollout safety, or observability -> `incident-response`
- Launch readiness, cross-functional execution, or release coordination -> `launch-readiness`
- Product framing, prioritization, or value tradeoffs -> `product-discovery`
- Broad review, ambiguous scope, or explicitly requested comprehensive feedback -> `full-team`

## Required Inputs

- Task statement.
- Optional decision to make.
- Optional constraints.
- Optional success metrics.
- Optional preset id or explicit persona subset.
- Optional model overrides by persona.
- Optional skill reference path/objective/mode.
- Optional comparison goal.
- Optional response depth (`brief`, `standard`, or `deep`).

If required context is missing, ask only the minimum clarification question needed to avoid a misleading recommendation. If the user does not answer, proceed with explicit assumptions.

## Selection Rules

- If `profileIds` are provided, use them exactly and skip preset selection.
- If a concrete preset is provided, load exactly that preset's profiles.
- If the preset is `auto` or omitted, apply the default experience rules.
- If the user explicitly asks for comprehensive, broad, or full-team review, prefer `full-team`.
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
- Pass the same task, decision, constraints, success metrics, comparison goal, and response depth to every route.
- Apply persona-specific framing only through the selected profile.
- Continue if one route fails; synthesize successful outputs and list missing routes.

Each routed invocation should include:

- Canonical task statement.
- Decision to make.
- Constraints.
- Success metrics.
- Persona profile name, role, experience, and personality.
- Resolved model and runner agent.
- Comparison goal.
- Response depth.

## Procedure

1. Normalize the task into one canonical statement.
2. Determine the decision the user is trying to make, even if it must be inferred.
3. Read the predefined manifest and resolve the selected profiles.
4. Build one invocation payload for the orchestrator containing task, decision, constraints, success metrics, preset/subset, overrides, comparison goal, and response depth.
5. Delegate execution to `run-task-with-personas`.
6. Let `run-task-with-personas` resolve model overrides and final runner agents.
7. Let `run-task-with-personas` invoke selected persona routes in parallel and return normalized outputs.
8. Compare proposals across risk, speed, maintainability, delivery confidence, and product impact when relevant.
9. Recommend one path and clearly state what would change the recommendation.

## Decision Rules

- If the user does not specify a comparison goal, default to `risk-first`.
- If multiple routes converge on the same recommendation, highlight the consensus instead of repeating identical detail.
- If outputs differ sharply, explain the conflict in terms of role incentives and hidden costs, not just wording differences.
- If a model override conflicts with supported routes, ignore the override and note it under assumptions.
- If more than half of the selected routes fail, stop short of a strong recommendation and report the run as incomplete.
- Prefer the smallest credible persona set that can answer the user's decision well.

## Output Format

Use this structure:

### Decision Snapshot
- Recommended route:
- Why it wins:
- Biggest risk to manage:
- Strongest alternative:
- Switch to the alternative when:
- Next move:

### Task
- Canonical task text:
- Decision to make:
- Constraints:
- Success metrics:
- Comparison goal:
- Response depth:
- Personas selected:

### Execution Matrix
- Persona name | Role | Default model | Final model | Runner agent | Route reason

### Per-Route Outputs
- Persona name:
  - Model:
  - Runner agent:
  - Skill reference used:
  - Skill applied:
  - Recommendation:
  - Best fit when:
  - Main risks:
  - Tradeoffs:
  - Validation checks:
  - First steps:
  - Definition of done:
  - Confidence:
  - Key assumptions:

### Synthesis
- Areas of agreement:
- Areas of disagreement:
- Recommended path:
- Strongest speed-first option:
- Strongest risk-first option:
- Strongest maintainability-first option:
- Rationale:
- Missing routes or failures:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

## Authoring Guidance

- Keep the task fixed once normalized.
- Use the manifest as the only source of truth for predefined routes.
- Do not fabricate model support or runner agent names.
- Prefer focused persona selection unless broad coverage is explicitly valuable.
- Make the synthesis decision-ready: name the winner, the main risk, and the reason to switch to the best alternative.
- Do not bypass `run-task-with-personas`; all runtime execution must be handed off to that agent.
