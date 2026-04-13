---
name: tdd-plan-first
description: "Start a TDD workflow with an explicit planning and requirements gathering phase before any code is written."
agent: "TDD Orchestrator"
---
Implement the following using strict test-driven development, starting with a thorough planning phase.

## Behavior
1. **Plan first**: analyze the request, search the codebase for context, and define behavior increments with testable acceptance criteria.
2. **Ask questions**: surface any ambiguity and ask follow-up questions before writing any code.
3. **Present the plan**: show the ordered list of behavior increments and acceptance criteria for approval.
4. **Execute TDD cycles**: for each approved increment, follow Red → Green → Refactor.
5. **Validate**: after each cycle, check that acceptance criteria are met.
6. **Repeat**: continue until all behavior is implemented.

## Inputs
- Feature or behavior to implement: {user provides}

## Rules
- Do not write any code until the plan is approved.
- Never write production code without a failing test.
- Never write more code than the tests require.
- Ask clarifying questions rather than making risky assumptions.
