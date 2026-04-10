# TDD agents

This directory contains a small set of GitHub Copilot agent definitions for running a strict Test-Driven Development workflow.

## Location

- Agent files: `TDD/agents`

## Agents

### `TDD`

The `TDD` agent is the orchestrator. It manages the overall Red → Green → Refactor loop and delegates each phase to a dedicated subagent.

Responsibilities:

- start the Red phase to define the next failing behavior
- start the Green phase to implement the smallest passing change
- start the Refactor phase to improve structure without changing behavior
- summarize each cycle and track validation status

### `TDD Red`

The `TDD Red` agent writes or updates tests only.

Responsibilities:

- identify the narrowest missing behavior
- add a focused failing test
- confirm the failure is caused by missing behavior
- hand control back to the `TDD` orchestrator

### `TDD Green`

The `TDD Green` agent changes production code only.

Responsibilities:

- read the failing Red-phase test
- make the smallest implementation change required
- run targeted validation when available
- hand control back to the `TDD` orchestrator

### `TDD Refactor`

The `TDD Refactor` agent improves code structure after tests are passing.

Responsibilities:

- make safe, minimal structural cleanups
- preserve externally visible behavior
- rerun relevant validation
- hand control back to the `TDD` orchestrator

## Workflow

The agents are designed to be used in this sequence:

1. `TDD` delegates to `TDD Red`
2. `TDD Red` returns to `TDD`
3. `TDD` delegates to `TDD Green`
4. `TDD Green` returns to `TDD`
5. `TDD` delegates to `TDD Refactor`
6. `TDD Refactor` returns to `TDD`

This cycle repeats until the requested behavior is fully implemented.
