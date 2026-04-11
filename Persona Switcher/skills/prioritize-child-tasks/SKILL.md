---
name: prioritize-child-tasks
description: 'Score and rank child tasks by delivery risk and critical-path impact to prioritize execution order. Use when: rank child tasks, identify critical path, prioritize delivery plan, sequence sprint work, highlight schedule risk.'
argument-hint: 'Provide child tasks, dependencies, optional weights, and any fixed milestone constraints.'
user-invocable: true
---

# Child Task Risk And Critical Path Scoring

## What This Skill Produces

This skill evaluates child tasks and returns:

1. Delivery-risk score per task.
2. Critical-path impact score per task.
3. Weighted priority ranking for execution planning.
4. Recommended sequencing and escalation focus.

## When To Use

- You already have one PBI with child tasks.
- You need a defensible order for implementation.
- You need to expose schedule threats before sprint execution.

## Required Inputs

- Child task list with IDs and titles.
- Dependencies between tasks.
- Optional effort estimate per task (S/M/L or numeric).
- Optional confidence level per task.
- Optional hard constraints (fixed milestone dates, mandated order).

If data is incomplete, score conservatively and record assumptions.

## Scoring Dimensions

Score each dimension on 1-5 where 5 means higher priority for planning attention.

- Delivery risk: Likelihood and severity of delay, rework, or failure.
- Critical-path impact: Degree to which delay in this task delays downstream completion.
- Dependency centrality: Number and importance of downstream tasks depending on it.
- Recovery difficulty: Difficulty of recovering schedule if this task slips.

## Default Weights

- Delivery risk: 0.40
- Critical-path impact: 0.35
- Dependency centrality: 0.15
- Recovery difficulty: 0.10

If the user explicitly requests speed-first sequencing:

- Critical-path impact: 0.45
- Dependency centrality: 0.25
- Delivery risk: 0.20
- Recovery difficulty: 0.10

## Procedure

1. Normalize tasks.
- Ensure each task has ID, title, and dependency references.
- Detect missing dependency links and record assumptions.

2. Build dependency graph.
- Identify entry tasks (no predecessors) and terminal tasks.
- Detect cycles and mark as blocking issues.

3. Apply hard constraints.
- Respect fixed milestone constraints and mandatory task order.
- Do not rank disallowed sequences above compliant sequences.

4. Score each task.
- Assign 1-5 scores for all dimensions.
- Use conservative scoring when information is uncertain.

5. Compute weighted total.
- Weighted total = sum(score_dimension x weight_dimension).
- Rank tasks highest to lowest weighted total.

6. Identify critical-path watchlist.
- Mark highest-impact tasks on or feeding the critical path.
- Flag top schedule-risk tasks requiring mitigation plans.

7. Recommend execution order.
- Provide a practical sequence respecting dependencies.
- Highlight tasks to parallelize where safe.

## Decision Rules

- If dependency cycles are found:
  - Mark ranking as provisional.
  - Recommend cycle resolution before final sequencing.

- If two tasks tie on weighted total:
  - Break ties in this order:
  - Higher critical-path impact
  - Higher delivery risk
  - Higher dependency centrality
  - Higher recovery difficulty

- If a task violates a hard constraint:
  - It cannot be prioritized ahead of required predecessor tasks.

## Quality Criteria

The workflow is complete only when all checks pass:

- All tasks are scored on all dimensions.
- Dependencies are represented and validated.
- Hard constraints are honored.
- Ranking table is complete and reproducible.
- Critical-path watchlist is explicit.
- Mitigation actions are listed for top risks.

## Output Format

### Inputs
- Tasks scored:
- Weights used:
- Hard constraints:

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

## Authoring Guidance

- Keep scoring rationale concise and evidence-based.
- Prefer dependency-aware prioritization over simple effort ordering.
- Mark uncertainty clearly; do not hide low-confidence inputs.
- Treat ranking as a planning aid, not a replacement for engineering judgment.
