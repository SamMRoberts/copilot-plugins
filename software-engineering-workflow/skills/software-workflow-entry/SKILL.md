---
name: software-workflow-entry
description: "Use when: standalone entry point that decides whether software work is new, resumed, or ambiguous, then routes to the right workflow agent. Use with the software-workflow-entry agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: true
---

# Software Workflow Entry

## Purpose

This skill is the discoverable companion for the `software-workflow-entry` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Standalone entry point that decides whether software work is new, resumed, or ambiguous, then routes to the right workflow agent.
- The user explicitly asks for the `software-workflow-entry` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `software-workflow-entry` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/software-workflow-entry.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `controller-entry`
- Parallel policy: `controller-sequential`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- User prompt

## Handoffs

- software-workflow-orchestrator (agent-determined): The prompt is clearly new work.
- work-resumption (agent-determined): The prompt refers to existing or interrupted work and no explicit phase was named.
- phase-specialist (user-choice): The user explicitly names a phase or chooses a continuation after resumption.

## Approval Gates

- None.

## Notes

Initial classifier. It does not implement code changes or build full plans except when asked only for routing advice.
