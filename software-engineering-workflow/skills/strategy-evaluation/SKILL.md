---
name: strategy-evaluation
description: "Use when: evaluating possible ways forward, comparing short-term expedient strategies against long-term durable strategies, selecting a pragmatic implementation path, assessing tradeoffs, avoiding over-engineering, and deciding what follow-up work is required when a short-term strategy is chosen. Use with the strategy-evaluation agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Strategy Evaluation

## Purpose

This skill is the discoverable companion for the `strategy-evaluation` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: evaluating possible ways forward, comparing short-term expedient strategies against long-term durable strategies, selecting a pragmatic implementation path, assessing tradeoffs, avoiding over-engineering, and deciding what follow-up work is required when a short-term strategy is chosen.
- The user explicitly asks for the `strategy-evaluation` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `strategy-evaluation` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/strategy-evaluation.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Requirements plus multiple viable paths or short-term/long-term tension

## Handoffs

- follow-up-work-items (agent-determined): A tactical or short-term path creates deferred obligations.
- solution-planning (agent-determined): A strategy is selected and ready to plan.
- user (user-choice): Strategy tradeoffs materially affect product behavior, risk, cost, or delivery.

## Approval Gates

- None.

## Notes

Keeps tactical choices explicit and prevents over-engineering.
