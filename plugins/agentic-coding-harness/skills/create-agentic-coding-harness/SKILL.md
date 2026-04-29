---
name: create-agentic-coding-harness
description: "Use when designing or creating a reusable harness for agentic coding work, including setup checks, context capture, execution phases, verification gates, and handoff artifacts. Do not use for ordinary feature implementation unless the task is to build or improve the harness itself."
argument-hint: "Describe the target repository, agent workflow, required checks, execution boundaries, and expected handoff artifacts."
---

# Create Agentic Coding Harness

Use this skill to define or improve a repeatable harness for agentic coding agents.

## Inputs

- Target repository or workspace.
- Agent workflow to support.
- Required context sources.
- Allowed and disallowed execution behavior.
- Verification commands or evidence expectations.
- Handoff format for completed work.

## Procedure

1. Identify the harness goal and the agent workflow it should support.
2. Define the setup contract: repository checks, dependency checks, environment assumptions, and required files.
3. Define the execution contract: phases, ownership boundaries, allowed tools, and when the agent must stop or ask.
4. Define the verification contract: commands to run, artifacts to inspect, and acceptable residual risk.
5. Define the handoff contract: summary, changed files, validation results, known gaps, and follow-up work.
6. Recommend the smallest durable implementation: guidance-only skill, hook, script, MCP server, or a combination.

## Output

Return a concise harness plan with:

- Harness purpose.
- Required inputs.
- Execution phases.
- Verification gates.
- Handoff artifacts.
- Proposed plugin files to create or update.
- Open questions that block implementation.
