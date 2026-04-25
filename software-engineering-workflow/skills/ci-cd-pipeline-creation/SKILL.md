---
name: ci-cd-pipeline-creation
description: "Use when: creating or updating CI/CD files after a pipeline plan exists, including GitHub Actions workflow YAML, Azure DevOps pipeline YAML, reusable workflow templates, pipeline templates, deployment jobs, environment gates, artifact publishing, cache steps, and validation automation. Use with the ci-cd-pipeline-creation agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# CI CD Pipeline Creation

## Purpose

This skill is the discoverable companion for the `ci-cd-pipeline-creation` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: creating or updating CI/CD files after a pipeline plan exists, including GitHub Actions workflow YAML, Azure DevOps pipeline YAML, reusable workflow templates, pipeline templates, deployment jobs, environment gates, artifact publishing, cache steps, and validation automation.
- The user explicitly asks for the `ci-cd-pipeline-creation` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `ci-cd-pipeline-creation` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/ci-cd-pipeline-creation.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `execution-phase`
- Parallel policy: `writer-sequential`
- Writes files: `true`
- Mutates repository state: `false`
- Runs commands: `true`

## Prerequisites

- Approved CI/CD plan including platform, permissions, secrets model, triggers, stages, and validation gates

## Handoffs

- ci-cd-pipeline-planning (agent-determined): Platform, deployment target, permissions, security model, or gates are missing.
- verification (agent-determined): Pipeline files are updated and need validation.
- user (approval-gated): The requested work would create secrets, grant permissions, change branch protection, or provision resources.

## Approval Gates

- Creating secrets
- Granting permissions
- Changing branch protection
- Provisioning cloud resources
- Configuring service connections

## Notes

Creates or updates workflow and pipeline files only after a plan exists.
