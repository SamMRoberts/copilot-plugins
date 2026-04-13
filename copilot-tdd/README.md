# copilot-tdd

A GitHub Copilot plugin that enforces strict test-driven development methodology using specialized agents, skills, and prompts.

## Overview

This plugin implements the full TDD cycle with an emphasis on **planning before coding**:

1. **Plan** — Analyze requirements, ask clarifying questions, define desired outcomes as testable acceptance criteria.
2. **Red** — Write failing tests that define the next behavior.
3. **Green** — Write the minimum production code to make tests pass.
4. **Refactor** — Improve structure while keeping tests green.
5. **Repeat** — Cycle through behavior increments until done.

## Components

### Agents

| Agent | Role | User-invocable |
|---|---|---|
| `TDD Orchestrator` | Manages the full workflow, asks user questions, validates phase gates | Yes |
| `TDD Planner` | Analyzes requirements, surfaces ambiguity, decomposes into increments | No |
| `TDD Red` | Writes failing tests only | No |
| `TDD Green` | Writes minimal production code only | No |
| `TDD Refactor` | Improves structure without changing behavior | No |

### Skills

| Skill | Description |
|---|---|
| `tdd-workflow` | Entry point for TDD workflows. Triggers on "TDD", "test-driven", "tests first", "red-green-refactor". |

### Prompts

| Prompt | Description |
|---|---|
| `tdd` | Quick-start TDD with a task description. |
| `tdd-plan-first` | Full planning phase with approval before any code is written. |

### Instructions

| File | Description |
|---|---|
| `instructions/copilot-instructions.md` | Global instructions that make TDD the preferred methodology. Copy to `.github/copilot-instructions.md` to activate repo-wide. |

## Installation

### As part of this repository

The agents, skills, and prompts are already available if this repo is your Copilot workspace.

### In another repository

1. Copy the `copilot-tdd/agents/` files to your repo's `.github/agents/`.
2. Copy the `copilot-tdd/skills/tdd-workflow/` directory to your repo's `.github/skills/tdd-workflow/`.
3. Copy the `copilot-tdd/prompts/` files to your repo's `.github/prompts/`.
4. Optionally, copy `copilot-tdd/instructions/copilot-instructions.md` to `.github/copilot-instructions.md` (or merge with existing).

## Workflow Sequence

```
User Request
    │
    ▼
┌─────────────────────┐
│  TDD Orchestrator    │
│  (Harness Discovery) │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  TDD Planner        │◄── Clarifying questions
│  (Requirements +    │     flow back through
│   Increments)       │     the Orchestrator
└────────┬────────────┘
         │
         ▼
    ┌────────────┐
    │  For each   │
    │  increment  │
    └────┬───────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  TDD Red        │───►│  TDD Green      │───►│  TDD Refactor   │
│  (Failing tests)│    │  (Minimal code) │    │  (Clean up)     │
└─────────────────┘    └─────────────────┘    └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Acceptance Gate  │
                                              │ (Criteria check) │
                                              └────────┬────────┘
                                                       │
                                               ┌───────┴───────┐
                                               │  Next         │
                                               │  increment?   │
                                               └───────────────┘
```

## Key Design Decisions

- **Orchestrator owns the user conversation.** Subagents produce artifacts; only the orchestrator asks the user questions. This prevents conversational state from fragmenting across agents.
- **Structured handoff payloads.** Every increment passed between agents follows a defined schema (see `references/handoff-schema.md`) to prevent scope drift.
- **Harness discovery before coding.** The orchestrator identifies the test framework and conventions before any TDD work begins.
- **Phase gates.** Each phase boundary is validated against a checklist to maintain TDD discipline.
- **Least-privilege tooling.** The planner has read-only tools; Red/Green/Refactor have edit + execute; the orchestrator has agent delegation.
