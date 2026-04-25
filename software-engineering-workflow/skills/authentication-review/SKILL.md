---
name: authentication-review
description: "Use when: reviewing an authentication plan, app sign-in design, Microsoft Entra ID design, Azure authentication setup, managed identity plan, OAuth/OIDC/SAML flow, session model, token handling, MFA, Conditional Access, secrets, or identity provider choice for security gaps and over-complexity before implementation. Use with the authentication-review agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Authentication Review

## Purpose

This skill is the discoverable companion for the `authentication-review` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: reviewing an authentication plan, app sign-in design, Microsoft Entra ID design, Azure authentication setup, managed identity plan, OAuth/OIDC/SAML flow, session model, token handling, MFA, Conditional Access, secrets, or identity provider choice for security gaps and over-complexity before implementation.
- The user explicitly asks for the `authentication-review` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `authentication-review` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/authentication-review.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Authentication plan

## Handoffs

- authentication-planning (agent-determined): Security gaps, maintainability risks, or over-complexity require rework.
- solution-planning (agent-determined): The auth plan is ready for implementation planning.
- user (user-choice): The user must accept residual auth risk or select between secure options.

## Approval Gates

- None.

## Notes

Catches auth security and complexity issues before implementation begins.
