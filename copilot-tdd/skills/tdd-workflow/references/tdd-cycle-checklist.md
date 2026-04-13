# TDD Cycle Checklist

Use this checklist to validate discipline at each phase boundary.

## Before Starting (Harness Discovery)

- [ ] Test framework identified (e.g., Jest, pytest, Go testing, xUnit).
- [ ] Test run command verified or discovered.
- [ ] Test file naming convention confirmed.
- [ ] Any required test setup or fixtures identified.
- [ ] If no test harness exists, setup is the first increment.

## Plan Phase Gate

- [ ] At least one behavior increment is defined.
- [ ] Each increment has acceptance criteria.
- [ ] Blocking questions are resolved or assumptions are stated.
- [ ] Increments are ordered by dependency.

## Red Phase Gate

- [ ] Only test files were modified.
- [ ] Each new test targets exactly one behavior from the increment.
- [ ] The test fails for the right reason (missing behavior, not syntax error).
- [ ] No production code was changed.

## Green Phase Gate

- [ ] Only production code was modified.
- [ ] The implementation is the smallest change that makes the failing test pass.
- [ ] No speculative features, abstractions, or cleanup were added.
- [ ] The Red-phase test now passes.
- [ ] Previously passing tests still pass.

## Refactor Phase Gate

- [ ] No new behavior was introduced.
- [ ] All tests still pass after refactoring.
- [ ] Changes improve clarity, reduce duplication, or simplify structure.
- [ ] No unnecessary changes were made.

## Acceptance Gate

- [ ] All acceptance criteria for the increment are satisfied by passing tests.
- [ ] The increment is deployable independently (no half-finished behavior).
- [ ] Decision made: proceed to next increment, re-plan, or stop.
