---
name: code-comment-audit
description: "Use when: auditing code comments after code changes, identifying key areas that need explanation, deciding what should document what/why/how, finding missing warnings about pitfalls, assumptions, tradeoffs, TODOs, invariants, edge cases, or complex control flow before editing comments. Always run after code changes to determine whether comments are needed. Use with the code-comment-audit agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Code Comment Audit

## Purpose

This skill is the discoverable companion for the `code-comment-audit` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: auditing code comments after code changes, identifying key areas that need explanation, deciding what should document what/why/how, finding missing warnings about pitfalls, assumptions, tradeoffs, TODOs, invariants, edge cases, or complex control flow before editing comments. Always run after code changes to determine whether comments are needed.
- The user explicitly asks for the `code-comment-audit` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `code-comment-audit` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/code-comment-audit.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `read-only-parallel-eligible`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Target code or scope plus maintainability/commenting objective
- Completed code changes requiring post-change audit before verification

## Handoffs

- code-comment-authoring (agent-determined): A comment plan is ready for scoped edits.
- solution-planning (agent-determined): Commenting needs should be included in broader implementation planning.
- documentation (agent-determined): The finding belongs in external docs rather than code comments.
- verification (agent-determined): The post-change audit finds no useful comment additions, revisions, or removals are needed.

## Approval Gates

- None.

## Notes

Read-only audit of where comments add maintainability value. It always runs after code changes before final verification. Parallel only when targets are independent.
