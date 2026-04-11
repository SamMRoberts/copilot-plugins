---
name: create-task-ready-brief
description: "Generate a task-ready brief with constraints, risks, and success metrics before running team-shared-task-perspectives."
argument-hint: "Describe the task, context, constraints, and what success should look like."
---
Create a task-ready brief that will be used as input to the `team-shared-task-perspectives` skill.

## Goal
Prepare a high-quality brief before persona analysis begins so all personas receive a complete, consistent assignment.

## Inputs To Infer Or Clarify
- Task statement
- Scope boundaries
- Technical constraints
- Timeline constraints
- Known dependencies
- Primary risks
- Success metrics

If key input is missing, make explicit assumptions instead of blocking.

## Output Format
Use exactly this structure:

### Task-Ready Brief
- Canonical task statement:
- Problem context:
- In scope:
- Out of scope:
- Constraints:
- Dependencies:
- Risks:
- Success metrics:
- Assumptions:
- Open questions:

### Ready-To-Run Invocation
Provide one copy-paste prompt for running `team-shared-task-perspectives` that includes:
- The canonical task statement
- Constraints
- Risks
- Success metrics
- Any assumptions that must remain visible

## Quality Checks
- The task statement is unambiguous and testable.
- Constraints are concrete, not generic.
- Risks are specific and actionable.
- Success metrics are measurable and time-bound when possible.
- Scope boundaries prevent personas from solving different problems.
