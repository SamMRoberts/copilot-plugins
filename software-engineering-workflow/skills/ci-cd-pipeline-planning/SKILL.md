---
name: ci-cd-pipeline-planning
description: "Use when: planning CI/CD automation for GitHub Actions, Azure DevOps Pipelines, GitLab CI, CircleCI, Jenkins, deployment gates, build/test/release stages, environments, artifacts, secrets, runners, service connections, or pipeline templates. Determines the optimal pipeline platform, triggers, stages, permissions, quality gates, deployment strategy, and validation plan before pipeline files are created. Use with the ci-cd-pipeline-planning agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# CI CD Pipeline Planning

## Purpose

This skill is the discoverable companion for the `ci-cd-pipeline-planning` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: planning CI/CD automation for GitHub Actions, Azure DevOps Pipelines, GitLab CI, CircleCI, Jenkins, deployment gates, build/test/release stages, environments, artifacts, secrets, runners, service connections, or pipeline templates. Determines the optimal pipeline platform, triggers, stages, permissions, quality gates, deployment strategy, and validation plan before pipeline files are created.
- The user explicitly asks for the `ci-cd-pipeline-planning` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `ci-cd-pipeline-planning` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/ci-cd-pipeline-planning.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Build, test, release, or deploy automation requirements and repository constraints

## Handoffs

- ci-cd-pipeline-creation (agent-determined): A pipeline plan includes platform, permissions, secrets model, triggers, stages, and gates.
- solution-planning (agent-determined): Pipeline decisions must be integrated into broader implementation planning.
- user (user-choice): Pipeline platform, deployment target, permissions, or approval gates require a decision.

## Approval Gates

- None.

## Notes

Plans automation but does not create workflow or pipeline YAML.
