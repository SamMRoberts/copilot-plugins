---
name: tdd-workflow
description: 'Use for test-driven development, TDD, writing tests first, red-green-refactor, behavior-driven implementation, or any request to build features using TDD methodology. Use when the user wants to write tests before code, implement with strict TDD discipline, or follow red-green-refactor cycles. Do not use for running existing tests, debugging test failures, or test-last workflows.'
argument-hint: 'Describe the feature, behavior, or change you want to implement using TDD.'
user-invocable: true
---

# TDD Workflow

## What This Skill Produces

A complete test-driven development workflow that:

1. Analyzes requirements and asks clarifying questions before writing any code.
2. Defines desired outcomes as testable acceptance criteria.
3. Decomposes work into ordered behavior increments.
4. Executes strict Red → Green → Refactor cycles for each increment.
5. Validates that acceptance criteria are met by passing tests.
6. Repeats until all requested behavior is implemented.

## When to Use

- Implementing a new feature or behavior.
- Adding functionality to existing code.
- Fixing a bug (write a failing test that reproduces it first).
- Any request where the user wants tests written before implementation.
- When the user mentions "TDD", "test-driven", "tests first", or "red-green-refactor".

## When NOT to Use

- Running or debugging existing tests (use standard test tools).
- Writing tests after implementation (test-last).
- Pure refactoring with no new behavior (use refactoring tools).
- Documentation-only changes.

## Required Inputs

- A description of the feature, behavior, or change to implement.
- Optional: specific acceptance criteria or edge cases.
- Optional: target files or modules.
- Optional: constraints (performance, compatibility, etc.).

If critical information is missing, the workflow will ask clarifying questions before proceeding.

## Procedure

1. **Delegate to the TDD Orchestrator agent.**
   Pass the user's request and any provided context. The orchestrator manages the full workflow.

2. **The orchestrator runs these phases:**
   - **Harness Discovery** — identifies the test framework, run command, and conventions.
   - **Planning** — delegates to the TDD Planner to analyze requirements, surface questions, define outcomes, and decompose into increments.
   - **Outcomes Discovery** — the planner systematically evaluates outcome categories (Core Logic, Interface/Delivery Surface, Integration, Input Validation, Error Handling, State Management, Access Control, Configuration) and builds an outcome matrix with IDs, priorities, and traceability to increments.
   - **Outcomes Review** — the orchestrator independently verifies category coverage, outcome-to-increment mapping, and test infrastructure needs.
   - **Clarification** — the orchestrator asks the user any blocking questions from the planner.
   - **Red** — delegates to TDD Red to write failing tests for one increment, at the correct test layer for the outcome category.
   - **Green** — delegates to TDD Green to write minimal passing code.
   - **Refactor** — delegates to TDD Refactor to improve structure.
   - **Acceptance Gate** — validates criteria are met, decides next action.
   - **Repeat** — cycles through remaining increments.

3. **Return the orchestrator output.**
   The final output includes cycle summaries, all tests added, all code changed, and any remaining follow-up items.

## Validation

Each phase is validated against the [TDD Cycle Checklist](./references/tdd-cycle-checklist.md):
- Outcomes Discovery: all applicable categories evaluated, must-outcomes mapped to increments, test infrastructure identified.
- Red: only test code changed, tests fail for the right reason, tests written at the correct layer.
- Green: only production code changed, tests pass, implementation is minimal.
- Refactor: no behavior changed, all tests still pass.
- Acceptance: criteria met, increment is independently complete.

## Output Format

Use the structure defined in [output-template.md](./references/output-template.md).
