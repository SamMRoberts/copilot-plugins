---
name: scope-creep-review
description: "Use when: checking scope creep by comparing the original ask, accepted requirements, current plan, changed files, implementation direction, or proposed follow-up work to ensure the work is not reaching beyond what is needed to satisfy the user's request. Flags overreach, unrelated refactors, speculative features, unnecessary abstractions, and work that should be deferred. Use with the scope-creep-review agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Scope Creep Review

## Purpose

This skill is the discoverable companion for the `scope-creep-review` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: checking scope creep by comparing the original ask, accepted requirements, current plan, changed files, implementation direction, or proposed follow-up work to ensure the work is not reaching beyond what is needed to satisfy the user's request. Flags overreach, unrelated refactors, speculative features, unnecessary abstractions, and work that should be deferred.
- The user explicitly asks for the `scope-creep-review` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `scope-creep-review` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/scope-creep-review.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Original ask plus requirements, plan, changed files, or proposed next steps

## Handoffs

- solution-planning (agent-determined): Scope findings should reshape the plan.
- follow-up-work-items (agent-determined): Useful but out-of-scope work should be deferred.
- user (user-choice): The user must accept or reject broader scope.

## Approval Gates

- None.

## Notes

Dedicated off-ramp for overreach, broad refactors, speculative features, and unnecessary abstractions.
