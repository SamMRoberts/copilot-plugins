---
name: team-decompose-to-pbi
description: "Have the full team analyze a task from every role perspective, then decompose the recommended approach into one sprint-ready PBI with child tasks. Use when: team input on backlog items, role-diverse planning before sprint, group decomposition, team-informed PBI creation."
argument-hint: "Describe the task, any constraints, timeline, and whether to use default or speed-first scoring."
agent: "run-team-perspectives"
---
Run this workflow in order and do not skip steps.

## Step 1: Run Team Perspectives
Use `run-team-perspectives` to generate persona proposals and synthesis for the task.

Each persona invocation must receive:
- The same canonical task statement
- The same constraints
- The same risks
- The same success metrics

Collect all per-persona outputs and produce the full synthesis including:
- Areas of agreement
- Areas of disagreement
- Recommended path
- Alternatives
- Rationale

Do not block the full run if one persona call fails; continue with completed outputs.

## Step 2: Select Recommended Approach
From the synthesis in Step 1, identify the recommended path.

Rules:
- Use the highest-ranked or consensus-recommended approach as the primary input to decomposition.
- If no clear consensus exists, use risk reduction as the tiebreaker.
- Carry forward constraints, risks, and success metrics from the team synthesis into the PBI.

## Step 3: Decompose Into One PBI And Child Tasks
Apply `create-pbi-and-tasks` using the recommended approach from Step 2 as the canonical task input.

Required output:
- Exactly one PBI
- Child Tasks table with Task ID, title, owner role, deliverable, dependencies, estimate, risk, completion signal
- Readiness Check
- Assumptions
- Open Questions

Rules:
- Keep one PBI only.
- If the recommended approach contains multiple outcomes, keep the primary one and move others to Future PBIs.
- Preserve any constraints and risks surfaced during the team perspectives run.

## Final Output Format
Use exactly this structure:

### Team Perspectives Summary
- Canonical task statement:
- Recommended approach:
- Key agreements:
- Key disagreements:
- Rationale for selection:

### PBI
- Title:
- User/Business value:
- In scope:
- Out of scope:
- Acceptance criteria:
- Non-functional requirements:
- Definition of done:

### Child Tasks
- Task ID | Task title | Owner role | Deliverable | Dependencies | Estimate (S/M/L) | Risk (L/M/H) | Completion signal

### Readiness Check
- Coverage of acceptance criteria:
- Dependency risks:
- Scope integrity check:
- Sprint readiness status:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

### Future PBIs (Optional)
- Candidate 1
