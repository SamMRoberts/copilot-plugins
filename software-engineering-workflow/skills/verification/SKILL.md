---
name: verification
description: "Use when: validates completed work, triages failures, summarizes residual risk, and decides whether work is complete or needs another phase. Use with the verification agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Verification

## Purpose

This skill is the discoverable companion for the `verification` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Validates completed work, triages failures, summarizes residual risk, and decides whether work is complete or needs another phase.
- The user explicitly asks for the `verification` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `verification` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/verification.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `validation-phase`
- Parallel policy: `verification-sequential`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `true`

## Prerequisites

- Implemented changes, pipeline/comment/Git changes, or resumed work needing completion assessment
- Post-change code comment audit completed when code changed

## Handoffs

- implementation (agent-determined): In-scope validation failures require fixes.
- solution-planning (agent-determined): Failures show the plan or requirements were incomplete.
- user (user-choice): Failures are outside scope, validation cannot run, or residual risk must be accepted.

## Approval Gates

- None.

## Notes

Terminal gate. It should validate after all mutations settle and after post-change code comment audit has completed for code changes.
