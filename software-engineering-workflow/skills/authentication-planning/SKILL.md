---
name: authentication-planning
description: "Use when: planning authentication strategy, sign-in, identity provider selection, local authentication, managed identity, cloud authentication, Microsoft Entra ID, Azure authentication, OAuth, OpenID Connect, SAML, MFA, Conditional Access, service-to-service auth, API auth, session handling, token flow, secrets, or passwordless access before implementation. Use with the authentication-planning agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Authentication Planning

## Purpose

This skill is the discoverable companion for the `authentication-planning` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: planning authentication strategy, sign-in, identity provider selection, local authentication, managed identity, cloud authentication, Microsoft Entra ID, Azure authentication, OAuth, OpenID Connect, SAML, MFA, Conditional Access, service-to-service auth, API auth, session handling, token flow, secrets, or passwordless access before implementation.
- The user explicitly asks for the `authentication-planning` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `authentication-planning` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/authentication-planning.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Authentication requirements, threat context, identity provider constraints, and environment constraints

## Handoffs

- authentication-review (agent-determined): An auth plan is ready for security and complexity review.
- solution-planning (agent-determined): The auth approach is accepted enough to plan implementation.
- ci-cd-pipeline-planning (agent-determined): The auth plan affects secrets, identities, service connections, or deployment automation.
- user (user-choice): Provider, consent, security posture, or operational ownership choices remain material.

## Approval Gates

- None.

## Notes

Plans authentication but does not create app registrations, secrets, credentials, service connections, or identity resources.
