---
name: run-task-with-personas-and-models
description: "Use when you want the same task reviewed or answered by multiple predefined personas — each with a distinct role, experience level, and assigned model. Good for: comparing engineering vs product vs SRE perspectives on a decision; getting side-by-side proposals before choosing an implementation path; evaluating a tradeoff from junior, mid, and senior viewpoints; discovering and incorporating skills referenced in the task across all persona routes; or any task where a single perspective isn't sufficient. Do not use to run a single-persona task or invoke one model directly."
argument-hint: "Provide the task, optional decision to make, optional preset or persona subset, optional model overrides, constraints, success metrics, optional skill names and/or a skill reference/objective/mode, and the decision you want from the comparison."
user-invocable: true
---

# Run Task With Personas And Models

## What This Skill Produces

This skill runs the same task against a curated set of predefined persona and model routes. It produces a decision-ready packet with:

1. A frozen canonical task statement used for every run.
2. A focused execution matrix showing persona, final model, and runner agent.
3. One isolated output per selected persona and model route.
4. A synthesis that names the best path, the strongest alternative, and the tradeoff that separates them.
5. Shared skill context that can be reused across persona routes when other skills are involved.

## Source Of Truth

Predefined persona and model routes are stored in [Predefined Persona-Model Profiles](./references/personas/predefined-persona-models.json).

For a quick role-to-model view, see [Persona To Model Mapping](./references/personas/persona-model-mapping.md).

That manifest defines:

- Available persona profiles.
- Default model per persona.
- Supported model override routes.
- Ready-made profile selection presets.

## Default Experience

Prefer focused reviews over a full-team blast unless the user explicitly asks for broad coverage.

If the user does not specify `profileIds` or a preset, resolve a focused preset automatically:

- Implementation, bug fix, test work, or code generation -> `engineering-core`
- Technical design, migration, refactor, or platform change -> `technical-design`
- Incident response, resilience, rollout safety, or observability -> `incident-response`
- Launch readiness, cross-functional execution, or release coordination -> `launch-readiness`
- Product framing, prioritization, or value tradeoffs -> `product-discovery`
- Broad review, ambiguous scope, or explicitly requested comprehensive feedback -> `full-team`

## Selection Rules

- If `profileIds` are provided, use them exactly and skip preset selection.
- If a concrete preset is provided, load exactly that preset's profiles.
- If the preset is `auto` or omitted, apply the default experience rules.
- If the user explicitly asks for comprehensive, broad, or full-team review, prefer `full-team`.
- If a requested persona is not in the manifest, do not invent a new profile; report it as unsupported.

## Routing Rules

Resolve each selected persona route in this order:

1. Explicit model override supplied by the user, if the model exists in `supportedModelRoutes`. Resolve to `persona-proposal-runner-<model>` agent.
2. The persona's `defaultModel` from the manifest. Resolve to `persona-proposal-runner-<model>` agent by naming convention.

Every route must resolve to a concrete model. If a persona has no `defaultModel` and no override is supplied, report it as a manifest error.

Do not change the canonical task text across routes.

## Execution Contract

- Runtime handoff is mandatory: always execute through `run-task-with-personas.agent.md` (agent name: `run-task-with-personas`).
- This skill is guidance and output-shape policy; it is not the runtime controller.
- When skill names or a skill reference are provided, `run-task-with-personas` should normalize that shared skill context once and pass it to every selected route.
- Run one isolated subagent call per selected persona.
- Keep each invocation stateless and independent.
- Pass the same task, decision, constraints, success metrics, comparison goal, and response depth to every route.
- Allow routes to reuse shared skill context and explain any route-specific interactions with the requested skills.
- Apply persona-specific framing only through the selected profile.
- Continue if one route fails; synthesize successful outputs and list missing routes.

When building the invocation payload in step 5, load [./references/invocation-contract.md](./references/invocation-contract.md) for the required fields.

## Procedure

1. **Discover skills from the prompt:** Before normalizing the task, scan the user's prompt for:
   - Explicit skill names or references (e.g., "using the X skill").
   - Implicit guidance requests (e.g., "follow best practices for...", "apply ...", "consider...").
   - Phrases suggesting skill execution mode: "must incorporate", "strictly require", or "essential" signal `required` mode; "optionally consider" or "may reference" signal `advisory` mode.
   - Skill objective hints from the prompt context.
2. Normalize the task into one canonical statement: restate as one declarative sentence in the imperative, resolve pronouns, remove conversational filler, and make the subject and scope explicit.
3. Determine the decision the user is trying to make, even if it must be inferred.
4. Read the predefined manifest and resolve the selected profiles. If any explicitly requested `profileIds` are not found in the manifest, report them as unsupported and exclude them from execution — do not invent or silently substitute profiles.
5. Build one invocation payload for the orchestrator containing task, decision, constraints, success metrics, preset/subset, overrides, optional skill inputs, comparison goal, and response depth.
6. Delegate the full invocation payload to `run-task-with-personas` and await its normalized outputs.
7. Post-process the synthesis returned by `run-task-with-personas` by applying the Decision Rules: group convergent routes, explain sharp conflicts in terms of role incentives and hidden costs, and name the recommended path and what would change it.
8. Load `./references/output-template.md` and render the final output, including a plain-language explanation of how route outputs were processed into the recommendation — covering weighting, tie-breaks, and excluded outliers — so the user can trace the decision logic.

## Decision Rules

- If the user does not specify a comparison goal, default to `risk-first`.
- If multiple routes converge on the same recommendation, highlight the consensus instead of repeating identical detail.
- If outputs differ sharply, explain the conflict in terms of role incentives and hidden costs, not just wording differences.
- If a model override conflicts with supported routes, ignore the override and note it under assumptions.
- If more than half of the selected routes fail, stop short of a strong recommendation and report the run as incomplete.
- Prefer the smallest credible persona set that can answer the user's decision well.

## Output Format

Load [./references/output-template.md](./references/output-template.md) before rendering.
