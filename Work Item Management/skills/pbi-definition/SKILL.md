---
name: pbi-definition
description: 'Draft one product backlog item from a high-level request or refined scope. Use for single-item backlog creation, scope definition, acceptance criteria, and dependency capture. Intended for delegation by orchestration skills. Do not use when child task breakdown is also needed — use backlog-item-decomposition for that.'
argument-hint: 'Provide the high-level request, constraints, and scope boundary.'
user-invocable: false
---

# PBI Definition

## Purpose

This skill creates one engineering-style product backlog item from a broader request.

It should produce:

- A single backlog item title.
- A clear type.
- A concise summary.
- In-scope and out-of-scope boundaries.
- Testable acceptance criteria.
- Dependencies and assumptions.
- A first-pass list of child-task candidates.

## When to Use

- A larger orchestration skill needs one backlog item drafted before task breakdown.
- The request needs to be reduced to one valuable slice.
- Acceptance criteria and scope boundaries need to be defined before child tasks are written.

## Procedure

1. Restate the requested outcome.
Identify the primary user or system value and the delivery boundary.

2. Choose the item type.
Classify as feature, bug, chore, spike, or technical improvement.

3. Define the smallest valuable slice.
If the request is broad, keep only the first coherent increment of value. Target a scope completable in one sprint and deployable independently.

4. Write the backlog item.
Create title, summary, in-scope statement, and out-of-scope statement.

5. Draft acceptance criteria.
Use observable outcomes, not low-level implementation instructions.

6. Capture dependencies and assumptions.
Call out blockers, upstream requirements, and any assumptions made while refining.

7. Propose child-task candidates.
List the likely implementation work areas as candidate tasks, but keep them distinct and concise so another skill can expand them.

## Quality Criteria

- Exactly one product backlog item is produced.
- The scope is explicit.
- Acceptance criteria are testable.
- Child-task candidates are distinct work areas, not duplicated activities.
- The item is small enough for one iteration.

## Output Format

### Product Backlog Item

- Title:
- Type:
- Summary:
- In scope:
- Out of scope:

### Acceptance Criteria

- Criterion 1
- Criterion 2
- Criterion 3

### Child-Task Candidates

- Candidate 1
- Candidate 2
- Candidate 3

### Dependencies

- Dependency 1

### Assumptions

- Assumption 1

### Open Questions

- Question 1
