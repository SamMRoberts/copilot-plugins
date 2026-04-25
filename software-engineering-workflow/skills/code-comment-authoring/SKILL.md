---
name: code-comment-authoring
description: "Use when: adding, updating, or removing code comments after a comment audit or approved plan exists. Writes concise comments that explain what, why, how, pitfalls, assumptions, invariants, TODOs, edge cases, and known problems without restating obvious code. Use with the code-comment-authoring agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Code Comment Authoring

## Purpose

This skill is the discoverable companion for the `code-comment-authoring` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: adding, updating, or removing code comments after a comment audit or approved plan exists. Writes concise comments that explain what, why, how, pitfalls, assumptions, invariants, TODOs, edge cases, and known problems without restating obvious code.
- The user explicitly asks for the `code-comment-authoring` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `code-comment-authoring` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/code-comment-authoring.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `execution-phase`
- Parallel policy: `writer-sequential`
- Writes files: `true`
- Mutates repository state: `false`
- Runs commands: `true`

## Prerequisites

- Comment audit or approved comment plan

## Handoffs

- code-comment-audit (agent-determined): Comment intent is unclear or the target set is not justified.
- verification (agent-determined): Comment edits are complete and need validation.

## Approval Gates

- None.

## Notes

Edits comments only and must not overlap with implementation or other file writers.
