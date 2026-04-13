---
name: tdd
description: "Start a TDD workflow — analyze requirements, write tests first, then implement."
agent: "TDD Orchestrator"
---
Implement the following using strict test-driven development.

## Behavior
1. First, analyze the request and codebase to plan behavior increments.
2. Ask clarifying questions if requirements are ambiguous.
3. For each increment, follow Red → Green → Refactor:
   - **Red**: write a failing test that defines the behavior.
   - **Green**: write the minimum code to make the test pass.
   - **Refactor**: improve structure while keeping tests green.
4. Repeat until all behavior is implemented.

## Inputs
- Feature or behavior to implement: {user provides}

## Rules
- Never write production code without a failing test.
- Never write more code than the tests require.
- Keep each increment small and independently valuable.
