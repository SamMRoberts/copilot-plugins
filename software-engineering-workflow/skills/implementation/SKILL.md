---
name: implementation
description: "Use when: performs scoped code and documentation changes after requirements, planning, review, and documentation preparation are complete. Use with the implementation agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Implementation

## Purpose

This skill is the discoverable companion for the `implementation` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Performs scoped code and documentation changes after requirements, planning, review, and documentation preparation are complete.
- The user explicitly asks for the `implementation` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `implementation` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/implementation.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `execution-phase`
- Parallel policy: `writer-sequential`
- Writes files: `true`
- Mutates repository state: `false`
- Runs commands: `true`

## Prerequisites

- Requirements
- Approved plan
- Review outcome
- Documentation decision

## Handoffs

- solution-planning (agent-determined): The plan is missing, stale, or conflicts with repository state.
- documentation (agent-determined): Documentation decision is missing or docs are part of the approved scope.
- code-comment-audit (agent-determined): Scoped code changes are complete and must be checked for comment needs before validation.
- user (approval-gated): The implementation requires destructive commands, broad rewrites, dependency changes, or reverting user changes outside the approved plan.

## Approval Gates

- Destructive commands
- Broad rewrites
- Dependency changes outside approved scope
- Reverting user changes
- Tests failing outside approved scope

## Notes

General executor. It must not begin until the prerequisite bundle is present, and it routes code changes through code-comment-audit before verification.
