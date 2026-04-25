---
name: git-advanced-operations
description: "Use when: planning or executing advanced Git commands such as interactive rebase, cherry-pick sequences, revert strategy, reflog recovery, bisect, worktree management, stash recovery, tags, submodules, sparse checkout, patch creation, branch surgery, or safe force-with-lease workflows. Use with the git-advanced-operations agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Git Advanced Operations

## Purpose

This skill is the discoverable companion for the `git-advanced-operations` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: planning or executing advanced Git commands such as interactive rebase, cherry-pick sequences, revert strategy, reflog recovery, bisect, worktree management, stash recovery, tags, submodules, sparse checkout, patch creation, branch surgery, or safe force-with-lease workflows.
- The user explicitly asks for the `git-advanced-operations` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `git-advanced-operations` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/git-advanced-operations.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `recovery-phase`
- Parallel policy: `git-sequential`
- Writes files: `false`
- Mutates repository state: `true`
- Runs commands: `true`

## Prerequisites

- Approved command plan and safety gates

## Handoffs

- verification (agent-determined): Advanced operation completes and the repository state should be validated.
- git-troubleshooting (agent-determined): The operation fails or reveals unexpected repository state.
- user (approval-gated): Commands rewrite history, delete data, discard changes, alter remotes, or publish rewritten history.

## Approval Gates

- History rewrite
- Data deletion
- Discarding changes
- Remote mutation
- Publishing rewritten history
- Branch or tag deletion

## Notes

Advanced Git executor with explicit command planning and safety gates.
