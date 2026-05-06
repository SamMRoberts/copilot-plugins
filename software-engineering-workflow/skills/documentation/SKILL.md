---
name: documentation
description: "Use when: plans and performs documentation work needed before or after implementation. Use with the documentation agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Documentation

## Purpose

This skill is the discoverable companion for the `documentation` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Plans and performs documentation work needed before or after implementation.
- The user explicitly asks for the `documentation` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `documentation` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/documentation.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `execution-phase`
- Parallel policy: `writer-sequential`
- Writes files: `true`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Requirements and plan plus a decision on user-facing or developer-facing documentation impact

## Handoffs

- implementation (agent-determined): Documentation preparation is complete and code changes are next.
- verification (agent-determined): The approved scope was documentation-only or docs were updated after implementation.
- user (user-choice): Documentation obligations are unclear or optional.

## Approval Gates

- None.

## Notes

Writes docs only when documentation preparation or update is part of the phase. It must not overlap with other writers.
