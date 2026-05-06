---
name: runtime-decision-review
description: "Use when: reviewing a proposed programming language, runtime, framework, platform, or execution model decision for fit, over-engineering, under-engineering, operational risk, team fit, security, maintainability, deployment impact, and whether it satisfies the original requirements. Use with the runtime-decision-review agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Runtime Decision Review

## Purpose

This skill is the discoverable companion for the `runtime-decision-review` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: reviewing a proposed programming language, runtime, framework, platform, or execution model decision for fit, over-engineering, under-engineering, operational risk, team fit, security, maintainability, deployment impact, and whether it satisfies the original requirements.
- The user explicitly asks for the `runtime-decision-review` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `runtime-decision-review` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/runtime-decision-review.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Proposed runtime choice plus rationale and requirements

## Handoffs

- runtime-options-assessment (agent-determined): The choice lacks evidence or is disproportionate.
- solution-planning (agent-determined): The runtime choice is approved or acceptable with noted risk.
- user (user-choice): The review exposes a material runtime tradeoff.

## Approval Gates

- None.

## Notes

Review gate for runtime fit, operational risk, security, maintainability, and scope control.
