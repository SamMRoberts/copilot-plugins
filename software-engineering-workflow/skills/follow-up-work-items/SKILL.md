---
name: follow-up-work-items
description: "Use when: converting a selected short-term strategy, workaround, expedited fix, known limitation, TODO, technical debt item, or deferred long-term improvement into concrete follow-up work items with scope, acceptance criteria, dependencies, priority, and timing guidance. Use with the follow-up-work-items agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Follow Up Work Items

## Purpose

This skill is the discoverable companion for the `follow-up-work-items` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: converting a selected short-term strategy, workaround, expedited fix, known limitation, TODO, technical debt item, or deferred long-term improvement into concrete follow-up work items with scope, acceptance criteria, dependencies, priority, and timing guidance.
- The user explicitly asks for the `follow-up-work-items` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `follow-up-work-items` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/follow-up-work-items.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Selected short-term workaround, deferred improvement, TODO, known limitation, or accepted debt

## Handoffs

- solution-planning (agent-determined): Deferred work is documented and the current scope can be planned.
- documentation (agent-determined): Follow-up work must be recorded in docs or release notes.

## Approval Gates

- None.

## Notes

Makes deferred work explicit so a short-term strategy does not silently become unmanaged debt.
