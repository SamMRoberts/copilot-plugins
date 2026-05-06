---
name: data-model-planning
description: "Use when: planning how to structure, organize, validate, analyze, or persist data across relational databases, NoSQL stores, Kusto/Azure Data Explorer tables, JSON, XML, YAML, APIs, configuration, documents, events, or file formats. Determines the optimal data representation, data type choices, schema boundaries, validation rules, query shape, ingestion shape, and evolution strategy before implementation. Use with the data-model-planning agent in the Software Engineering Workflow plugin."
argument-hint: "Provide the request, relevant context, known prerequisites, and desired output or continuation point."
user-invocable: false
---

# Data Model Planning

## Purpose

This skill is the discoverable companion for the `data-model-planning` agent. It should load when the task belongs to this Software Engineering Workflow phase and should keep the route table as the source of truth.

## When To Use

- Use when: planning how to structure, organize, validate, analyze, or persist data across relational databases, NoSQL stores, Kusto/Azure Data Explorer tables, JSON, XML, YAML, APIs, configuration, documents, events, or file formats. Determines the optimal data representation, data type choices, schema boundaries, validation rules, query shape, ingestion shape, and evolution strategy before implementation.
- The user explicitly asks for the `data-model-planning` phase, or a controller routes here from `software-workflow-entry`, `software-workflow-orchestrator`, or `work-resumption`.

## Procedure

1. Check `software-engineering-workflow/workflow-routes.json` for this phase's prerequisites, handoffs, approval gates, and parallel policy.
2. Delegate execution to the `data-model-planning` agent and pass the user request, gathered evidence, route metadata, constraints, and expected output.
3. Keep the phase boundary narrow. Do not perform downstream specialist work inside this skill unless agent invocation is unavailable.
4. If the agent cannot be invoked, load `software-engineering-workflow/agents/data-model-planning.agent.md` and follow that agent's instructions directly.
5. Return the agent's artifacts, findings, open questions, approval needs, and recommended next handoff to the controller or user.

## Route Contract

- Role: `read-only-phase`
- Parallel policy: `sequential-decision`
- Writes files: `false`
- Mutates repository state: `false`
- Runs commands: `false`

## Prerequisites

- Data, schema, API contract, event, file, or configuration requirements

## Handoffs

- solution-planning (agent-determined): The data model is ready to integrate into the implementation plan.
- documentation (agent-determined): Schema, contract, or migration behavior must be documented.
- user (user-choice): Data shape, migration, compatibility, or persistence tradeoffs remain material.

## Approval Gates

- None.

## Notes

Plans data representation and schema decisions but does not create migrations or implementation code.
