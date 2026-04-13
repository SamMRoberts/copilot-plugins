---
name: backlog-item-decomposition
description: 'Use when breaking down a high-level work item into a bounded product backlog item with non-overlapping child tasks. Use for backlog refinement, sprint planning, story slicing, acceptance criteria, and dependency analysis. Do not use when only a single PBI without task breakdown is needed — use pbi-definition for that.'
argument-hint: 'Paste the high-level work item, constraints, and any known scope boundaries.'
user-invocable: true
---

# Backlog Item Decomposition

## What This Skill Produces

This skill acts as an entrypoint and dispatcher. It defers execution to the `Work Item Orchestrator` agent, which turns a high-level request into:

1. One well-bounded product backlog item.
2. A set of child tasks drafted in parallel from that backlog item.
3. A final pass that removes overlap and clarifies boundaries across child tasks.
4. Acceptance criteria, dependencies, assumptions, and open questions.

The output should favor a single deliverable backlog item, not an epic split into multiple peer stories unless the user explicitly asks for that.

The delegated agent should use these skills for specialized drafting work:

- `pbi-definition` for creation of the single product backlog item.
- `child-task-definition` for creation of each child task.

## When to Use

- A request is too broad to execute directly.
- A feature, bug fix, or technical change needs refinement before implementation.
- The team needs a story-sized backlog item with child tasks created consistently.
- Scope, dependencies, or acceptance criteria are unclear.
- A work item needs to be sliced so it fits in one iteration.
- Child tasks should be generated in parallel and then deconflicted.

## Required Inputs

- The high-level work item.
- Any hard constraints such as deadline, architecture, team ownership, or non-functional requirements.
- Optional context such as user persona, target system, dependencies, or current implementation state.

If critical information is missing, make the minimum reasonable assumptions, label them clearly, and ask only the highest-value follow-up questions.

## Orchestration Workflow

0. Signal decomposition start.
Write an immediate kickoff status message in the check or chat context to confirm the workflow has begun, for example: "Backlog decomposition started: normalizing request and drafting product backlog item."

1. Delegate execution to the `Work Item Orchestrator` agent.
Pass the high-level work item, constraints, and output expectations to the agent and instruct it to run its full workflow.

2. Let the orchestrator run decomposition.
The agent should normalize the request, coordinate parallel persona subagents, and use `pbi-definition` and `child-task-definition` through those personas.

3. Return orchestrator output.
Return the finalized package produced by the agent: one PBI, non-overlapping child tasks, overlap check notes, dependencies, assumptions, and open questions.

4. Retry once if orchestration fails.
If delegation fails, retry agent invocation with a shorter normalized input and explicit constraints.

5. Fallback only if agent invocation is unavailable.
If the `Work Item Orchestrator` agent cannot be invoked, invoke `pbi-definition` and `child-task-definition` directly using the inputs above.

## Output Format

Use the structure defined in [output-template.md](./references/output-template.md).


