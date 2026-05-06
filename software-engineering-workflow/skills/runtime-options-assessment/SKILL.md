---
name: runtime-options-assessment
description: "Use when: assessing new objectives and requirements to choose the best programming language, runtime, platform, framework, or execution model, including C#, .NET, Rust, Go, C++, TypeScript, JavaScript, Node.js, Deno, Bun, Python, Java, JVM, WebAssembly, native, serverless, containerized, desktop, CLI, mobile, embedded, or browser runtimes. Use with the runtime-options-assessment agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Runtime Options Assessment

## Purpose

This skill is the discoverable companion for the `runtime-options-assessment` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: assessing new objectives and requirements to choose the best programming language, runtime, platform, framework, or execution model, including C#, .NET, Rust, Go, C++, TypeScript, JavaScript, Node.js, Deno, Bun, Python, Java, JVM, WebAssembly, native, serverless, containerized, desktop, CLI, mobile, embedded, or browser runtimes.
- The user explicitly asks for the `runtime-options-assessment` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `runtime-options-assessment` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/runtime-options-assessment.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Objectives and requirements involving language, runtime, framework, platform, or execution model

## Handoffs

- runtime-decision-review (agent-determined): A runtime recommendation is ready for focused review.
- solution-planning (agent-determined): The runtime choice is straightforward or already accepted.
- user (user-choice): Runtime options affect operations, cost, migration, or team support.

## Approval Gates

- None.

## Notes

Produces the runtime recommendation but does not create scaffolding or implementation code.
