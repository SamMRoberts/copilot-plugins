---
name: plan-review
description: "Use when: reviews proposed plans for missed requirements, hidden risks, runtime fit, test gaps, sequencing issues, and unnecessary scope. Use with the plan-review agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Plan Review

## Purpose

This skill is the discoverable companion for the `plan-review` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Reviews proposed plans for missed requirements, hidden risks, runtime fit, test gaps, sequencing issues, and unnecessary scope.
- The user explicitly asks for the `plan-review` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `plan-review` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/plan-review.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Concrete implementation plan

## Handoffs

- solution-planning (agent-determined): Plan findings require revision before implementation.
- scope-creep-review (agent-determined): The main concern is drift from the original ask.
- runtime-decision-review (agent-determined): The main concern is runtime, platform, framework, or execution model fit.
- documentation (agent-determined): The plan is ready and documentation preparation should happen before implementation.
- user (user-choice): The user must accept residual risk or choose between plan changes.

## Approval Gates

- None.

## Notes

Pre-implementation review gate for bugs, behavioral regressions, sequencing risks, and test gaps.
