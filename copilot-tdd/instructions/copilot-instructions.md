# TDD Methodology — Copilot Instructions

When implementing features, fixing bugs, or adding behavior, prefer test-driven development:

## Default Workflow

1. **Understand before coding.** Analyze the request, search the codebase for context, and identify the test framework and conventions.
2. **Clarify ambiguity.** Ask follow-up questions about scope, edge cases, and error handling rather than guessing.
3. **Discover outcomes systematically.** Evaluate outcome categories (Core Logic, Interface/Delivery Surface, Integration, Input Validation, Error Handling, State Management, Access Control, Configuration) against the request. Build an outcome matrix with IDs and priorities. Ensure user-facing artifacts have Interface-layer outcomes.
4. **Write the test first (Red).** Create a focused failing test that defines one behavior. Test at the correct layer for the outcome category — interface outcomes need interface-level tests (e.g., HTTP tests), not just unit tests. Confirm it fails for the right reason.
5. **Write the minimum code (Green).** Implement only enough production code to make the failing test pass. No speculative features.
6. **Improve structure (Refactor).** Clean up duplication, naming, and complexity while keeping all tests passing.
7. **Repeat.** Move to the next behavior increment and cycle again.

## When to Apply TDD

- New feature implementation.
- Bug fixes (write a failing test that reproduces the bug first).
- Adding behavior to existing code.
- Any task where the user requests TDD, tests-first, or red-green-refactor.

## When NOT to Force TDD

- Documentation changes.
- Configuration-only changes.
- Exploratory debugging.
- Pure refactoring where existing test coverage is already comprehensive.

## Discipline Rules

- Never write production code without a corresponding failing test.
- Never write more code than the current tests require.
- Keep increments small — one behavior per Red → Green → Refactor cycle.
- Run tests after every phase change to catch regressions immediately.
- If scope changes mid-implementation, pause and re-plan before continuing.

## Invoking the TDD Workflow

Use the `tdd-workflow` skill or the `tdd` / `tdd-plan-first` prompts to activate the full TDD workflow with planning, orchestration, and phase subagents.
