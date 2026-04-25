---
name: work-resumption
description: "Use when: reconstructs existing work state and recommends the precise workflow phase where the user should continue. Use with the work-resumption agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: true
---

# Work Resumption

## Purpose

This skill is the discoverable companion for the `work-resumption` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Reconstructs existing work state and recommends the precise workflow phase where the user should continue.
- The user explicitly asks for the `work-resumption` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `work-resumption` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/work-resumption.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `controller-resumption`
- Parallel policy: `controller-sequential`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Resumed-work prompt or existing workspace state to reconstruct

## Handoffs

- best-continuation-phase (agent-determined): Evidence clearly shows the next phase.
- alternative-continuation-phase (user-choice): Multiple reasonable continuation points exist.

## Approval Gates

- None.

## Notes

State reconstructor and continuation recommender. It does not perform implementation.
