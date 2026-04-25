---
name: solution-planning
description: "Use when: produces scoped implementation plans from requirements and discovery findings before code changes begin. Use with the solution-planning agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Solution Planning

## Purpose

This skill is the discoverable companion for the `solution-planning` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Produces scoped implementation plans from requirements and discovery findings before code changes begin.
- The user explicitly asks for the `solution-planning` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `solution-planning` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/solution-planning.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Accepted requirements plus relevant specialty plans, reviews, and constraints

## Handoffs

- plan-review (agent-determined): A concrete implementation plan is ready for critique.
- documentation (agent-determined): The plan needs documentation preparation before implementation.
- user (user-choice): The plan has material sequencing, risk, or scope tradeoffs.

## Approval Gates

- None.

## Notes

Fan-in point for requirements and specialty phase outputs before implementation.
