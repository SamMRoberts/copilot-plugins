---
name: git-troubleshooting
description: "Use when: diagnosing Git problems, confusing repository state, failed pull/push/fetch/merge/rebase/cherry-pick, detached HEAD, diverged branches, lock files, missing commits, remote/auth issues, submodule problems, line ending churn, or unexpected diffs. Use with the git-troubleshooting agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Git Troubleshooting

## Purpose

This skill is the discoverable companion for the `git-troubleshooting` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: diagnosing Git problems, confusing repository state, failed pull/push/fetch/merge/rebase/cherry-pick, detached HEAD, diverged branches, lock files, missing commits, remote/auth issues, submodule problems, line ending churn, or unexpected diffs.
- The user explicitly asks for the `git-troubleshooting` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `git-troubleshooting` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/git-troubleshooting.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `recovery-phase`
- Parallel policy: `git-sequential`
- Writes files: `false`
- Mutates repository state: `true`
- Runs commands: `true`

## Prerequisites

- Failed Git command, confusing repository state, visible divergence, lock, remote/auth issue, or unexpected diff

## Handoffs

- git-conflict-resolution (agent-determined): Unmerged files or semantic conflicts are the blocker.
- git-advanced-operations (approval-gated): Recovery requires advanced or history-affecting Git operations.
- verification (agent-determined): Repository state is repaired and needs validation.
- user (user-choice): Multiple recovery paths have different risk profiles.

## Approval Gates

- Mutating Git commands
- Destructive cleanup
- History rewrite
- Force push
- Discarding changes

## Notes

Defaults to read-only diagnosis, but is considered Git-sequential because it may be asked to fix state.
