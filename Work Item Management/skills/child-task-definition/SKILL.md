---
name: child-task-definition
description: 'Draft one child task from a product backlog item and a specific task candidate. Use for implementation-oriented task creation, task boundary definition, dependency capture, and done criteria. Intended for parallel delegation by orchestration skills. Do not use for drafting the parent product backlog item — use pbi-definition for that.'
argument-hint: 'Provide the parent backlog item context and one child-task candidate.'
user-invocable: false
---

# Child Task Definition

## Purpose

This skill creates one child task from an existing product backlog item and one candidate work area.

It should optimize for:

- One primary purpose per task.
- Clear boundaries.
- Minimal overlap with sibling tasks.
- Explicit done criteria.
- Self-contained — implementable without sibling-task context.

## When to Use

- A parent product backlog item already exists.
- A coordinator is generating multiple child tasks in parallel.
- Each task must be independently understandable and implementable.

## Required Inputs

- Parent backlog item title and summary.
- Parent acceptance criteria.
- Parent scope boundaries.
- One child-task candidate.
- Known dependencies or sequencing constraints, if any.

## Procedure

1. Restate the candidate in the context of the parent PBI.
Anchor the task to the backlog item outcome.

2. Define the task boundary.
Specify the concrete deliverable this task owns and what it explicitly does not own.

3. Draft done criteria.
Describe the conditions that make the task complete.

4. Note dependencies.
Identify prerequisite work and downstream impact.

5. Check for probable overlap.
Avoid broad wording that would absorb work from sibling tasks, especially testing, documentation, shared API changes, or rollout activity unless that is the task's main purpose.

## Output Format

### Child Task

- Title:
- Purpose:
- In scope:
- Out of scope:
- Done criteria:
- Dependencies:
- Overlap risk:
