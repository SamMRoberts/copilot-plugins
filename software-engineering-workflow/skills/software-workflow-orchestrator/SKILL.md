---
name: software-workflow-orchestrator
description: "Use when: orchestrates new software work through discovery, requirements, strategy evaluation, scope control, runtime selection, authentication, data modeling, CI/CD planning, Git workflow management, code commenting, planning, review, documentation, implementation, and verification. Use with the software-workflow-orchestrator agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: true
---

# Software Workflow Orchestrator

## Purpose

This skill is the discoverable companion for the `software-workflow-orchestrator` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Orchestrates new software work through discovery, requirements, strategy evaluation, scope control, runtime selection, authentication, data modeling, CI/CD planning, Git workflow management, code commenting, planning, review, documentation, implementation, and verification.
- The user explicitly asks for the `software-workflow-orchestrator` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `software-workflow-orchestrator` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/software-workflow-orchestrator.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `controller-orchestrator`
- Parallel policy: `controller-sequential`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `true`

## Prerequisites

- New-work classification or direct user invocation for new work

## Handoffs

- context-discovery (agent-determined): Facts, relevant files, constraints, or risks are unknown.
- requirements-synthesis (agent-determined): Enough facts exist to define scope and acceptance criteria.
- specialty-phase (agent-determined): The accepted scope involves strategy, runtime, authentication, data, CI/CD, Git, or comment decisions.
- solution-planning (agent-determined): Requirements and needed specialty decisions are ready for implementation planning.
- implementation (agent-determined): Requirements, plan, review outcome, and documentation decision are complete.
- user (user-choice): Material tradeoffs affect behavior, cost, security, data migration, destructive operations, or accepted risk.

## Approval Gates

- Destructive operations
- Reverting user changes
- Dependency changes outside the approved plan
- Verification failures outside the approved scope

## Notes

Main conversation owner for new work. It coordinates fan-out and fan-in and keeps specialists from competing for the user thread.
