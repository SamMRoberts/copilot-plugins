---
name: context-discovery
description: "Use when: performs read-only discovery across the prompt, repository, constraints, risks, and existing implementation patterns. Use with the context-discovery agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Context Discovery

## Purpose

This skill is the discoverable companion for the `context-discovery` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Performs read-only discovery across the prompt, repository, constraints, risks, and existing implementation patterns.
- The user explicitly asks for the `context-discovery` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `context-discovery` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/context-discovery.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `read-only-parallel-eligible`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- User prompt or resumed-work state

## Handoffs

- requirements-synthesis (agent-determined): Facts are sufficient to define scope.
- solution-planning (agent-determined): The request is already scoped and needs an implementation plan.

## Approval Gates

- None.

## Notes

Only this phase is broadly parallel-eligible, and only across independent read-only surfaces.
