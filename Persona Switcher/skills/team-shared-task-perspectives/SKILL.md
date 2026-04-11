---
name: team-shared-task-perspectives
description: 'Assign the same task to the whole team so each member responds from a unique pre-defined persona (role, experience, personality), then synthesize perspectives. Use when you want to assign a task to the team, have each team member provide instructions for the same prompt, compare role-based viewpoints, run multi-persona analysis, backlog refinement, solution design, risk analysis, or implementation planning. Trigger examples: "assign a task to the team", "have each member provide instructions", "ask all team members the same question", "how would each role answer this", "assign how to make a peanut butter and jelly sandwich to each team member".'
argument-hint: 'Provide the shared task and constraints. The skill uses pre-defined team personas and returns full proposals by default.'
user-invocable: false
---

# Team Shared Task Perspectives

## What This Skill Produces

This skill assigns the same task text to every team member while preserving each member's unique pre-defined persona. It produces:

1. A normalized shared task statement used verbatim for all members.
2. Persona-scoped outputs from each team member.
3. A synthesis highlighting agreement, disagreement, risks, and recommended next action.

## Invocation Model

- Primary entrypoint is the `run-team-perspectives` agent.
- This skill is policy and output-shape guidance for orchestrator and persona worker agents.
- Do not use this skill as the runtime controller for parallel execution.

## When to Use

- You want every engineer to approach the exact same task from different perspectives.
- You need role-diverse planning without changing task scope per person.
- You are running design reviews, implementation planning, or risk workshops.
- You need traceable evidence that all members received identical instructions.

## Required Inputs

- Shared task statement.
- Optional constraints (timeline, architecture boundaries, non-functional requirements).
- Optional override for synthesis policy (for example, speed-first instead of risk-first).
- Optional injected skills list to be passed to the execution agent (for example, domain-specific skills that should be applied during persona generation or synthesis).

Team and persona definitions are pre-defined in this skill and applied automatically.

## Execution Contract

- `run-team-perspectives` is responsible for runtime execution and parallel fan-out.
- The canonical shared task, global constraints, and synthesis policy must be passed unchanged to persona workers.
- If injected skills are provided, pass them through the orchestrator to each persona worker as additive execution guidance.
- If no injected skills are provided, run with the default persona workflow only.

## Invocation Payload

Use this normalized payload shape when invoking `run-team-perspectives`:

```json
{
  "sharedTask": "Provide instructions for how to make a peanut butter and jelly sandwich.",
  "globalConstraints": [
    "Keep scope fixed to one sandwich",
    "Use plain household ingredients and tools",
    "Do not change canonical task text per persona"
  ],
  "risks": [
    "Task ambiguity",
    "Persona output convergence"
  ],
  "successMetrics": [
    "All personas receive identical task text",
    "Distinct per-persona outputs",
    "Synthesis includes recommendation and alternatives"
  ],
  "synthesisPolicy": "risk-first",
  "injectedSkills": [
    "optional-skill-1",
    "optional-skill-2"
  ]
}
```

Notes:
- Omit `injectedSkills` when none are needed.
- Injected skills are additive guidance only and must not alter scope or hard constraints.
- Preserve `sharedTask` verbatim across all persona invocations.
- Source of truth for execution details: `./.github/agents/run-team-perspectives.agent.md`.

## Persona Model

Use this pre-defined team structure with modular persona fields:

- Role: Functional accountability.
- Experience: Seniority and domain depth.
- Personality: Working style that influences tradeoffs.

Pre-defined personas are loaded from dedicated resource files:

- Machine-readable index: [Persona Index JSON](./references/personas/index.json)

- [Software Engineer (Junior)](./references/personas/software-engineer-junior.md)
- [Software Engineer (Mid-level)](./references/personas/software-engineer-mid-level.md)
- [Software Engineer (Senior)](./references/personas/software-engineer-senior.md)
- [Site Reliability Engineer (Junior)](./references/personas/site-reliability-engineer-junior.md)
- [Site Reliability Engineer (Mid-level)](./references/personas/site-reliability-engineer-mid-level.md)
- [Site Reliability Engineer (Senior)](./references/personas/site-reliability-engineer-senior.md)
- [Engineering Manager](./references/personas/engineering-manager.md)
- [Program Manager](./references/personas/program-manager.md)
- [Product Manager](./references/personas/product-manager.md)

Do not change the shared task text across personas.

## Procedure

1. Normalize task text.
- Rewrite the task once for clarity if needed.
- Freeze that final text as the canonical assignment.

2. Validate persona coverage.
- Load the pre-defined persona files listed in Persona Model.
- If the user supplies custom personas, map them to the same modular fields and label any assumptions.

2.5. Build orchestrator execution payload.
- Prepare one payload containing:
  - Canonical shared task text
  - Global constraints
  - Synthesis policy override (if provided)
  - Injected skills list (if provided)
- Validate that injected skills are explicitly listed and treated as additive guidance, not scope changes.

3. Broadcast identical assignment.
- Send the exact same canonical task text to every member.
- Include only global constraints common to all members.

4. Generate persona-specific responses.
- Each member responds from their persona lens only.
- Keep scope fixed; vary approach, risks, sequence, and emphasis.
- Produce full proposals for each member, not brief checklists.

5. Capture outputs in a consistent schema.
- Proposed approach
- Key risks
- Tradeoffs
- First implementation steps
- Definition of done from that persona

6. Synthesize and deconflict.
- Group overlaps and disagreements.
- Resolve conflicts by explicit decision rules.
- Produce one recommendation and alternatives.

7. Final quality check.
- Confirm assignment text was identical for all members.
- Confirm perspectives are meaningfully distinct.
- Confirm synthesis maps back to each member output.
- Confirm execution occurred via `run-team-perspectives` with the final canonical task and any injected skills.

## Decision Rules

- If task is ambiguous:
  - Ask the minimum high-impact clarification questions.
  - If unanswered, proceed with assumptions and label them.

- If personas converge too closely:
  - Increase persona contrast by refining personality or experience depth.

- If outputs conflict on architecture or sequence:
  - Prefer options that satisfy hard constraints first.
  - Then optimize for risk reduction first.
  - Only prioritize delivery speed first when the user explicitly requests it.

- If one persona proposes out-of-scope work:
  - Move it to "Future Considerations" and keep the shared task unchanged.

- If injected skills conflict with hard constraints or immutable shared task scope:
  - Keep hard constraints and shared task immutable.
  - Apply injected skills only as execution guidance.
  - Record the conflict under assumptions.

## Quality Criteria

The workflow is complete only when all checks pass:

- Every member received the exact same canonical task statement.
- Every member has all three persona modules.
- Outputs are distinct in perspective but aligned to one scope.
- Risks and tradeoffs are explicit per member.
- Final synthesis includes recommendation, alternatives, and rationale.
- Assumptions and open questions are clearly listed.
- Execution was performed by `run-team-perspectives` with required payload fields.
- Any injected skills used during execution are listed for traceability.

## Output Format

Use this structure:

### Shared Task
- Canonical task text:
- Global constraints:
- Injected skills (optional):

### Team Personas
- Software Engineer (Junior): role | experience | personality
- Software Engineer (Mid-level): role | experience | personality
- Software Engineer (Senior): role | experience | personality
- Site Reliability Engineer (Junior): role | experience | personality
- Site Reliability Engineer (Mid-level): role | experience | personality
- Site Reliability Engineer (Senior): role | experience | personality
- Engineering Manager: role | experience | personality
- Program Manager: role | experience | personality
- Product Manager: role | experience | personality

### Per-Member Outputs
- Member name:
  - Approach:
  - Risks:
  - Tradeoffs:
  - First steps:
  - Definition of done:

### Synthesis
- Areas of agreement:
- Areas of disagreement:
- Recommended path:
- Alternatives:
- Rationale:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

## Authoring Guidance

- Keep the task text immutable once normalized.
- Avoid assigning different subtasks unless explicitly requested.
- Emphasize perspective differences, not scope differences.
- Prefer concrete actions over abstract commentary.
- Default to full proposals per persona.
- Use risk reduction as the default synthesis tie-breaker unless explicitly overridden.
- Always execute through `run-team-perspectives`; do not use this skill as a parallel runtime controller.
- Treat injected skills as optional execution augmentations and document which were applied.
