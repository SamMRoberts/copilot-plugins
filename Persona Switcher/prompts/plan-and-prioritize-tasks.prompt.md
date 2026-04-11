---
name: plan-and-prioritize-tasks
description: "Run end-to-end planning: decompose a request into one PBI with child tasks, then score and rank child tasks by delivery risk and critical-path impact."
argument-hint: "Provide the request, constraints, dependencies, and whether to use default or speed-first weighting."
---
Run this workflow in order and do not skip steps.

## Step 1: Decompose Into One PBI And Child Tasks
Apply `create-pbi-and-tasks` to the user request.

Required output from this step:
- Exactly one PBI
- Child Tasks table with Task ID, title, owner role, deliverable, dependencies, estimate, risk, completion signal
- Readiness Check
- Assumptions
- Open Questions

Rules:
- Keep one PBI only.
- If the request contains multiple outcomes, keep the primary one and move others to Future PBIs.
- If information is missing, make explicit assumptions and continue.

## Step 2: Build Scoring Input
Prepare a normalized scoring input from Step 1 output.

Required fields:
- Child task list with IDs and titles
- Dependencies between tasks
- Hard constraints (if provided)
- Weight profile

Weight profile:
- Use default weights unless user explicitly requests speed-first.
- Default:
  - Delivery risk: 0.40
  - Critical-path impact: 0.35
  - Dependency centrality: 0.15
  - Recovery difficulty: 0.10
- Speed-first:
  - Critical-path impact: 0.45
  - Dependency centrality: 0.25
  - Delivery risk: 0.20
  - Recovery difficulty: 0.10

## Step 3: Score And Rank Child Tasks
Apply `prioritize-child-tasks` using the normalized input from Step 2.

Requirements:
- Validate dependencies before ranking.
- If dependency cycles are detected, mark ranking provisional and continue.
- Honor hard constraints before ranking.
- Include critical path watchlist with mitigations.

## Final Output Format
Use exactly this structure:

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

### Ranking Table
- Task ID | Task title | Delivery risk | Critical-path impact | Dependency centrality | Recovery difficulty | Weighted total | Rank

### Critical Path Watchlist
- Task ID | Reason | Suggested mitigation

### Recommended Sequence
- Sequence steps:
- Parallelization opportunities:
- Constraint notes:

### Assumptions
- Assumption 1

### Open Questions
- Question 1

### Final Recommendation
- Prioritized first tasks:
- Why these first:
- Runner-up priorities:
- Tradeoff summary:
- Sensitivity notes:
