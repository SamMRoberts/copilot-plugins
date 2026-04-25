---
name: git-conflict-resolution
description: "Use when: resolving merge conflicts, rebase conflicts, cherry-pick conflicts, revert conflicts, deconflicting concurrent edits, choosing semantic conflict resolutions, preserving user changes, or preparing conflicted files for verification. Use with the git-conflict-resolution agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Git Conflict Resolution

## Purpose

This skill is the discoverable companion for the `git-conflict-resolution` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: resolving merge conflicts, rebase conflicts, cherry-pick conflicts, revert conflicts, deconflicting concurrent edits, choosing semantic conflict resolutions, preserving user changes, or preparing conflicted files for verification.
- The user explicitly asks for the `git-conflict-resolution` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `git-conflict-resolution` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/git-conflict-resolution.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `recovery-phase`
- Parallel policy: `git-sequential`
- Writes files: `true`
- Mutates repository state: `true`
- Runs commands: `true`

## Prerequisites

- Actual conflict state or approved conflict-resolution workflow

## Handoffs

- code-comment-audit (agent-determined): Conflicts changed code and the result needs post-change comment audit before validation.
- git-troubleshooting (agent-determined): Repository state remains confusing or blocked after resolution.
- user (approval-gated): A resolution would discard one side, run destructive cleanup, reset, restore, checkout, or force-push.

## Approval Gates

- Discarding either side of a conflict
- Whole-file ours/theirs
- Reset
- Restore
- Checkout cleanup
- Force push

## Notes

Semantic conflict resolver. It can edit conflicted files but must preserve user work and avoid destructive shortcuts.
