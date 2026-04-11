---
name: create-pbi-and-tasks
description: 'Decompose a request into one Product Backlog Item (PBI) and its child Tasks with clear scope, acceptance criteria, dependencies, estimates, and Definition of Done. Use when: break down work, create backlog item, split epic/request into tasks, agile planning, sprint-ready decomposition.'
argument-hint: 'Provide the task/request, constraints, timeline, team context, and any non-functional requirements.'
user-invocable: true
---

# Decompose Task To PBI And Child Tasks

## What This Skill Produces

This skill converts a single request into:

1. One canonical Product Backlog Item (PBI).
2. A set of child Tasks that fully implement that PBI.
3. A readiness check showing whether the work is sprint-ready.

## When To Use

- You have one request and need one backlog-ready PBI.
- You need clear child task boundaries for implementation, QA, and release.
- You want acceptance criteria and dependencies made explicit before sprint planning.

## Required Inputs

- Task or request statement.
- Optional constraints (deadline, architecture boundaries, compliance, tooling).
- Optional non-functional requirements (security, performance, reliability, accessibility).
- Optional team context (roles available, capacity assumptions).

If key inputs are missing, proceed with explicit assumptions.

## Procedure

1. Normalize the request.
- Rewrite the request once into a clear canonical objective.
- Keep scope singular: one PBI only.

2. Define PBI boundaries.
- Identify in-scope outcomes and out-of-scope items.
- State user/business value in one sentence.
- Add acceptance criteria that are testable.

3. Identify decomposition dimensions.
- Split work by lifecycle: design, implementation, validation, release readiness.
- Add cross-cutting tasks only when required by constraints (for example security hardening).

4. Create child Tasks.
- Each task must have one owner role, one primary deliverable, and one completion signal.
- Keep tasks independently verifiable.
- Avoid tasks that are only status labels (for example "Do development").

5. Add sequencing and dependencies.
- Mark predecessor tasks where strict order is required.
- Keep parallelizable work parallel.
- Call out external dependencies and blocking risks.

6. Estimate and risk-rate.
- Assign relative size (S, M, L) and risk (Low, Medium, High) per task.
- Flag any task with High risk and include mitigation.

7. Run readiness checks.
- Verify child tasks collectively satisfy all PBI acceptance criteria.
- Verify no child task changes the PBI scope.
- Verify Definition of Done is explicit for PBI and each child task.

## Decision Rules

- If the request appears to contain multiple outcomes:
  - Select the primary outcome for this PBI.
  - Move additional outcomes to "Future PBIs".

- If acceptance criteria are ambiguous:
  - Add measurable placeholders and mark assumptions.

- If decomposition is too coarse:
  - Split tasks until each has a concrete deliverable and clear verification step.

- If decomposition is too fine-grained:
  - Merge micro-tasks that cannot be independently validated.

- If constraints conflict with scope:
  - Preserve scope first, then adjust sequencing, implementation approach, or assumptions.

## Quality Criteria

The workflow is complete only when all checks pass:

- Exactly one PBI is defined.
- PBI value statement is clear.
- Acceptance criteria are testable.
- Child tasks are complete and non-overlapping.
- Dependencies and sequencing are explicit.
- Risks and mitigations are captured.
- PBI and child-task Definition of Done are explicit.

## Output Format

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

## Authoring Guidance

- Keep one PBI per invocation.
- Prefer concrete verbs and testable criteria.
- Use assumptions instead of blocking when input is incomplete.
- Keep child tasks implementation-focused and independently verifiable.
