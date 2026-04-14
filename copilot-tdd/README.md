# copilot-tdd

A GitHub Copilot plugin that enforces strict test-driven development methodology using specialized agents, skills, and prompts.

## Overview

This plugin implements the full TDD cycle with an emphasis on **planning before coding**:

1. **Plan** — Analyze requirements, ask clarifying questions, define desired outcomes as testable acceptance criteria.
2. **Discover Outcomes** — Systematically evaluate outcome categories (Core Logic, Interface, Integration, Error Handling, etc.) and build a traceable outcome matrix.
3. **Red** — Write failing tests that define the next behavior, at the correct test layer for the outcome category.
4. **Green** — Write the minimum production code to make tests pass.
5. **Refactor** — Improve structure while keeping tests green.
6. **Repeat** — Cycle through behavior increments until done.

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

### Hooks

Agent hooks provide deterministic, enforceable controls at key lifecycle points during TDD sessions. Unlike prompt-based instructions, hooks execute as shell scripts and cannot be ignored by the model.

| Hook | Event | Purpose |
|---|---|---|
| `hooks/session-start.sh` | `sessionStart` | Initializes TDD audit log and cycle state tracking |
| `hooks/pre-tool-guard.sh` | `preToolUse` | Protects methodology files and lock files from accidental modification |
| `hooks/post-tool-tracker.sh` | `postToolUse` | Tracks file edits and test executions for TDD cycle audit trail |
| `hooks/post-tool-format.sh` | `postToolUse` | Auto-formats code after edits using the project's detected formatter |
| `hooks/session-end-summary.sh` | `sessionEnd` | Generates a TDD session summary with cycle statistics |
| `hooks/error-logger.sh` | `errorOccurred` | Logs errors to the TDD audit trail for debugging |

**Audit log**: Hooks write structured JSONL logs to `.tdd-logs/session.jsonl` in the working directory. This directory is excluded from git via `.gitignore`.

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
4. Copy the `copilot-tdd/hooks/` directory and `copilot-tdd/hooks.json` to your repo's `.github/hooks/` and `.github/hooks.json`.
5. Optionally, copy `copilot-tdd/instructions/copilot-instructions.md` to `.github/copilot-instructions.md` (or merge with existing).
6. Ensure `.tdd-logs/` is in your `.gitignore`.

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
│   Outcomes Discovery│     the Orchestrator
│   + Increments)     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Orchestrator       │
│  (Outcomes Review   │◄── Verifies category coverage,
│   Gate)             │     outcome-to-increment mapping,
└────────┬────────────┘     test infrastructure needs
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
│  (Failing tests │    │  (Minimal code) │    │  (Clean up)     │
│   @ right layer)│    └─────────────────┘    └────────┬────────┘
└─────────────────┘                                    │
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
- **Deterministic hooks.** Agent hooks enforce hard constraints (protected files, audit logging, auto-formatting) that cannot be overridden by the model, complementing the soft guidance in agent instructions.
