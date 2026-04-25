---
name: requirements-synthesis
description: "Use when: converts prompt and discovery findings into scoped requirements, acceptance criteria, assumptions, and open questions. Use with the requirements-synthesis agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Requirements Synthesis

## Purpose

This skill is the discoverable companion for the `requirements-synthesis` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Converts prompt and discovery findings into scoped requirements, acceptance criteria, assumptions, and open questions.
- The user explicitly asks for the `requirements-synthesis` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `requirements-synthesis` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/requirements-synthesis.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Prompt plus discovery findings or enough user-provided context

## Handoffs

- strategy-evaluation (agent-determined): Multiple approaches or short-term versus long-term tradeoffs exist.
- solution-planning (agent-determined): Requirements and acceptance criteria are ready.
- user (user-choice): Required scope or acceptance criteria remain ambiguous.

## Approval Gates

- None.

## Notes

Requirements decisions should be made once per stable scope before downstream planning.
