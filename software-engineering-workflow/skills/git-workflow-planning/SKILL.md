---
name: git-workflow-planning
description: "Use when: planning Git workflow, branch strategy, commit structure, pull request hygiene, release branching, repository collaboration, history policy, merge versus rebase decisions, stash/worktree usage, or Git best practices before changing repository state. Use with the git-workflow-planning agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Git Workflow Planning

## Purpose

This skill is the discoverable companion for the `git-workflow-planning` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: planning Git workflow, branch strategy, commit structure, pull request hygiene, release branching, repository collaboration, history policy, merge versus rebase decisions, stash/worktree usage, or Git best practices before changing repository state.
- The user explicitly asks for the `git-workflow-planning` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `git-workflow-planning` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/git-workflow-planning.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `git-sequential`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Repository collaboration, branch, commit, history, release, or review objective

## Handoffs

- implementation (agent-determined): The workflow plan affects how edits should be organized.
- git-conflict-resolution (agent-determined): The workflow plan encounters or anticipates semantic conflicts.
- git-advanced-operations (approval-gated): The workflow plan requires history rewriting, force-with-lease, or other advanced Git operations.
- user (user-choice): Branch policy, history shape, collaboration risk, or publication timing requires user choice.

## Approval Gates

- Rewriting published history
- Force-with-lease
- Branch or tag deletion
- Remote changes

## Notes

Plans Git workflow but does not run mutating Git commands or edit files.
