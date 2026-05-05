#!/usr/bin/env python3
"""Initialize an agentic coding harness in the current repository.

This script asks a guided series of questions, then writes:
- AGENTS.md
- docs/ harness, design, execution-plan, app-spec, reference, and validation docs

It avoids overwriting existing files unless --force is passed.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
from pathlib import Path
import re
import sys
from textwrap import dedent

ROOT = Path.cwd()

DEFAULTS = {
    "project_name": "This project",
    "purpose": "Document the project purpose here.",
    "users": "Document the primary users or operators here.",
    "agent_scope": "Documentation updates, tests, small fixes, and scoped implementation work with clear acceptance criteria.",
    "out_of_scope": "Production credential changes, destructive data operations, unapproved architecture rewrites, and work not represented in the harness scope.",
    "approval_required": "Security model changes, public API changes, data migrations, dependency swaps, deployment changes, and scope expansion.",
    "domains": "Core application, developer tooling, documentation, validation harness.",
    "architecture": "Types -> Config -> Repo -> Service -> Runtime -> UI, with cross-cutting providers entering through explicit interfaces.",
    "tech_stack": "Document languages, frameworks, runtimes, package managers, and deployment targets here.",
    "commands": "Document format, lint, test, typecheck, build, and local startup commands here.",
    "observability": "Document local app startup, logs, metrics, traces, screenshots, DOM snapshots, or other agent-legible validation workflows here.",
    "constraints": "Document non-negotiable security, privacy, reliability, compliance, and operational constraints here.",
    "doc_locations": "Design docs: docs/design-docs/. Execution plans: docs/exec-plans/. App specs: docs/app-specs/. References: docs/references/.",
    "plan_process": "Active plans live in docs/exec-plans/active/. Completed plans move to docs/exec-plans/completed/. Technical debt is tracked in docs/exec-plans/tech-debt-tracker.md.",
    "quality": "Prefer legible, tested, documented patterns; validate data at boundaries; avoid hidden coupling; keep future agent runs easy to reason about.",
}

QUESTIONS = [
    ("project_name", "Project or product name", DEFAULTS["project_name"]),
    ("purpose", "One-sentence project purpose", DEFAULTS["purpose"]),
    ("users", "Primary users or operators", DEFAULTS["users"]),
    ("agent_scope", "Work explicitly in scope for coding agents", DEFAULTS["agent_scope"]),
    ("out_of_scope", "Work explicitly out of scope", DEFAULTS["out_of_scope"]),
    ("approval_required", "Changes requiring explicit human approval", DEFAULTS["approval_required"]),
    ("domains", "Major product domains or app areas", DEFAULTS["domains"]),
    ("architecture", "Architecture layers or dependency boundaries", DEFAULTS["architecture"]),
    ("tech_stack", "Language, framework, runtime, and package manager conventions", DEFAULTS["tech_stack"]),
    ("commands", "Commands for format, lint, tests, builds, type checks, and startup", DEFAULTS["commands"]),
    ("observability", "Local app, UI, logs, metrics, traces, or validation workflows", DEFAULTS["observability"]),
    ("constraints", "Security, privacy, reliability, or compliance constraints", DEFAULTS["constraints"]),
    ("doc_locations", "Where docs should be filed", DEFAULTS["doc_locations"]),
    ("plan_process", "How plans and technical debt should be maintained", DEFAULTS["plan_process"]),
    ("quality", "Top quality or taste invariants", DEFAULTS["quality"]),
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "project"


def ask_questions(non_interactive: bool, answers_file: Path | None) -> dict[str, str]:
    answers = dict(DEFAULTS)

    if answers_file:
        loaded = json.loads(answers_file.read_text(encoding="utf-8"))
        for key, value in loaded.items():
            if key in answers and str(value).strip():
                answers[key] = str(value).strip()

    if non_interactive:
        return answers

    print("Agentic coding harness initialization")
    print("Press Enter to keep the default shown in brackets.\n")

    for key, label, default in QUESTIONS:
        current = answers.get(key, default)
        raw = input(f"{label} [{current}]: ").strip()
        if raw:
            answers[key] = raw

    return answers


def bullets(text: str) -> list[str]:
    parts = [p.strip(" -") for p in re.split(r"[\n;]+", text) if p.strip(" -")]
    if len(parts) == 1 and "," in parts[0]:
        parts = [p.strip(" -") for p in parts[0].split(",") if p.strip(" -")]
    return parts or ["Document this further."]


def md_bullets(text: str) -> str:
    return "\n".join(f"- {item}" for item in bullets(text))


def write(path: Path, content: str, force: bool, written: list[Path], skipped: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        skipped.append(path)
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    written.append(path)


def render_agents(a: dict[str, str]) -> str:
    # Intentionally line-oriented and close to 100 lines.
    return dedent(
        f"""
        # AGENTS.md

        ## Purpose

        This file is the routing map for coding agents working on {a['project_name']}.
        Project purpose: {a['purpose']}
        Keep this file short; put durable project knowledge in `docs/`.

        ## Harness rule

        Before code edits, read this file, then `docs/harness/scope.md`.
        Do not edit code that conflicts with the harness, is out of scope,
        or is not included in the harness scope.

        ## Table of contents

        | Context | Read first |
        | --- | --- |
        | Harness scope, exclusions, approvals | `docs/harness/scope.md` |
        | Initialization answers and setup history | `docs/harness/initialization.md` |
        | Agent operating model | `docs/harness/operating-model.md` |
        | Documentation map | `docs/README.md` |
        | Product intent and users | `docs/app-specs/app-spec.md` |
        | Product specs index | `docs/app-specs/index.md` |
        | Architecture and boundaries | `docs/architecture.md` |
        | Design docs and decisions | `docs/design-docs/index.md` |
        | Core engineering beliefs | `docs/design-docs/core-beliefs.md` |
        | Active plans | `docs/exec-plans/active/` |
        | Plan template | `docs/exec-plans/plan-template.md` |
        | Completed plans | `docs/exec-plans/completed/` |
        | Technical debt | `docs/exec-plans/tech-debt-tracker.md` |
        | Commands, tools, package manager | `docs/tooling.md` |
        | Quality bar and invariants | `docs/quality.md` |
        | Security constraints | `docs/security.md` |
        | Reliability constraints | `docs/reliability.md` |
        | Logs, metrics, traces, UI validation | `docs/observability.md` |
        | Review expectations | `docs/review.md` |
        | External or copied references | `docs/references/index.md` |

        ## Scope gate

        Classify every requested code change before editing.

        - `IN_SCOPE`: allowed by `docs/harness/scope.md`.
        - `NEEDS_PLAN`: allowed, but requires an execution plan.
        - `HARNESS_UPDATE_REQUIRED`: useful, but not currently included.
        - `OUT_OF_SCOPE`: explicitly excluded.
        - `CONFLICTS_WITH_HARNESS`: violates a harness rule.

        Proceed only for `IN_SCOPE`, or `NEEDS_PLAN` after creating/reading a plan.

        ## Blocked-change response

        When blocked, do not patch code. Respond with:

        ```text
        Harness gate blocked this change.
        Reason: <specific doc/rule that blocks it>
        Resolution options:
        1. Update the harness scope/docs, then create a new plan.
        2. Stop this task with no changes.
        3. Create a new in-scope plan that satisfies the current harness.
        ```

        ## Planning requirements

        Create an active plan for multi-file, architectural, security, reliability,
        or user-visible behavior changes.

        Active plans live in `docs/exec-plans/active/`.
        Completed plans move to `docs/exec-plans/completed/`.
        Use `docs/exec-plans/plan-template.md`.

        ## Documentation requirements

        Update docs when a change affects product behavior, architecture,
        commands, validation, scope, security, reliability, or quality rules.

        Add design docs under `docs/design-docs/`.
        Add execution plans under `docs/exec-plans/`.
        Add app specs under `docs/app-specs/`.
        Add reference docs under `docs/references/`.

        ## Architecture requirements

        Preserve these boundaries: {a['architecture']}
        Do not add cross-layer imports or hidden coupling that bypasses documented boundaries.
        When architecture needs to change, update docs first and create an execution plan.

        ## Validation requirements

        Run the commands listed in `docs/tooling.md` for the files you changed.
        If commands cannot run, explain why and record the risk in the plan or final response.
        Do not invent validation results.

        ## Quality requirements

        Follow `docs/quality.md` for naming, file size, testing, logging,
        schema validation, and maintainability expectations.
        Prefer shared utilities and documented patterns over one-off helpers.

        ## Security and reliability

        Follow `docs/security.md` and `docs/reliability.md`.
        Do not weaken auth, validation, privacy, rate limits, retries, timeouts,
        observability, or error handling without explicit harness approval.

        ## References

        Use `docs/references/` for external docs copied into the repo.
        Prefer repo-local references over relying on inaccessible chat history or memory.

        ## Drift control

        If code and docs disagree, stop and identify the discrepancy.
        Ask whether to update docs, update code, or create a new execution plan.
        Record recurring issues in `docs/exec-plans/tech-debt-tracker.md`.
        """
    ).strip()


def render_docs(a: dict[str, str]) -> dict[str, str]:
    today = _dt.date.today().isoformat()
    project_slug = slugify(a["project_name"])

    return {
        "docs/README.md": f"""
# Documentation Map

This folder is the system of record for coding agents working on `{a['project_name']}`.

## Required folders

- `harness/`: scope, initialization, and operating model.
- `design-docs/`: decisions, design history, and core beliefs.
- `exec-plans/`: active plans, completed plans, and technical debt.
- `app-specs/`: product requirements and user-facing behavior.
- `references/`: external or copied reference material made repo-local.

## Required top-level docs

- `architecture.md`: layers and dependency boundaries.
- `tooling.md`: commands and validation workflows.
- `quality.md`: quality bar and taste invariants.
- `security.md`: security and privacy constraints.
- `reliability.md`: reliability and operational expectations.
- `observability.md`: logs, metrics, traces, UI, and app-legibility workflows.
- `review.md`: review loop and merge expectations.

Update this map when docs are added, moved, retired, or replaced.
""",
        "docs/harness/scope.md": f"""
# Harness Scope

## Project

- Name: {a['project_name']}
- Purpose: {a['purpose']}
- Primary users/operators: {a['users']}

## In scope for coding agents

{md_bullets(a['agent_scope'])}

## Out of scope for coding agents

{md_bullets(a['out_of_scope'])}

## Requires explicit human approval

{md_bullets(a['approval_required'])}

## Scope gate

Before any code change, classify the request:

- `IN_SCOPE`: allowed by this document and not conflicting with any harness rule.
- `NEEDS_PLAN`: allowed, but requires an execution plan before implementation.
- `HARNESS_UPDATE_REQUIRED`: useful, but not currently included in scope.
- `OUT_OF_SCOPE`: explicitly excluded by this document.
- `CONFLICTS_WITH_HARNESS`: violates documented architecture, product, quality, security, reliability, validation, or process constraints.

Only `IN_SCOPE` work may proceed directly. `NEEDS_PLAN` work may proceed after an active plan is created or read.

## Blocked-change response

If a request is `HARNESS_UPDATE_REQUIRED`, `OUT_OF_SCOPE`, or `CONFLICTS_WITH_HARNESS`, do not edit code. Respond with:

```text
Harness gate blocked this change.
Reason: <specific doc/rule that blocks it>
Resolution options:
1. Update the harness scope/docs, then create a new plan.
2. Stop this task with no changes.
3. Create a new in-scope plan that satisfies the current harness.
```

If the user chooses to update the harness, update documentation first. Do not implement the originally blocked code change until the updated harness clearly permits it.
""",
        "docs/harness/initialization.md": f"""
# Harness Initialization

Initialized: {today}
Project slug: `{project_slug}`

## Captured answers

| Question | Answer |
| --- | --- |
| Project or product name | {a['project_name']} |
| One-sentence purpose | {a['purpose']} |
| Primary users/operators | {a['users']} |
| Agent in-scope work | {a['agent_scope']} |
| Agent out-of-scope work | {a['out_of_scope']} |
| Approval-required changes | {a['approval_required']} |
| Product domains/app areas | {a['domains']} |
| Architecture boundaries | {a['architecture']} |
| Tech stack conventions | {a['tech_stack']} |
| Validation commands | {a['commands']} |
| Observability workflows | {a['observability']} |
| Security/reliability constraints | {a['constraints']} |
| Documentation locations | {a['doc_locations']} |
| Plan process | {a['plan_process']} |
| Quality invariants | {a['quality']} |

## Reinitialization rule

Do not overwrite these answers silently. When project direction changes, update the relevant docs and add a dated note explaining the change.
""",
        "docs/harness/operating-model.md": f"""
# Agent Operating Model

## Human and agent roles

Humans steer. Agents execute inside the harness.

Humans provide goals, acceptance criteria, approval for scope changes, and final judgment when the harness is incomplete or contradictory.

Agents read the harness, create plans when required, implement in-scope work, validate outcomes, and update docs when project knowledge changes.

## Agent workflow

1. Read `AGENTS.md`.
2. Read `docs/harness/scope.md`.
3. Route to task-specific docs from the AGENTS table of contents.
4. Classify the task with the scope gate.
5. Create an execution plan when required.
6. Make the smallest in-scope change.
7. Run relevant validation commands.
8. Update docs and indexes when knowledge changes.
9. Report results, skipped validation, and remaining risks.

## Missing capability rule

When an agent cannot complete a task reliably, do not retry blindly. Identify whether the missing capability is documentation, tooling, architecture, tests, observability, or scope. Propose a harness update or execution plan.
""",
        "docs/design-docs/index.md": """
# Design Docs Index

Design docs capture durable decisions, tradeoffs, and architecture/product rationale.

## Docs

- `core-beliefs.md`: agent-first engineering principles.

## Add a design doc when

- architecture changes;
- product behavior needs rationale;
- a tradeoff should be preserved for future agent runs;
- repeated review feedback should become reusable guidance.
""",
        "docs/design-docs/core-beliefs.md": f"""
# Core Beliefs

## Agent legibility

Anything important for coding agents must be visible in the repository. Chat threads, memory, and external docs do not count unless summarized or copied into `docs/`.

## Repository as system of record

Project knowledge should live in versioned markdown, schemas, code, tests, scripts, plans, and references.

## Constraints over micromanagement

Enforce boundaries, correctness, reproducibility, and maintainability. Within those constraints, allow implementation flexibility.

## Feedback loops

When quality issues repeat, convert them into docs, tests, linters, scripts, or execution-plan checks.

## Project-specific quality invariants

{md_bullets(a['quality'])}
""",
        "docs/exec-plans/index.md": """
# Execution Plans Index

Execution plans are first-class repo artifacts.

## Folders

- `active/`: plans currently being implemented.
- `completed/`: plans moved here after validation.
- `plan-template.md`: required plan shape.
- `tech-debt-tracker.md`: known drift, stale docs, missing checks, and cleanup work.

Create a plan before multi-file, architectural, security, reliability, or user-visible behavior changes.
""",
        "docs/exec-plans/active/README.md": """
# Active Execution Plans

Store active plans here.

Use `../plan-template.md`.

Move completed plans to `../completed/` after validation.
""",
        "docs/exec-plans/completed/README.md": """
# Completed Execution Plans

Move completed plans here after implementation and validation.

Keep completed plans for historical context and future agent runs.
""",
        "docs/exec-plans/plan-template.md": """
# Execution Plan: <title>

## Status

- State: active
- Owner: coding agent
- Created: <date>
- Last updated: <date>

## Summary

Describe the task in one paragraph.

## Scope

### In scope

- <item>

### Out of scope

- <item>

## Harness docs consulted

- `AGENTS.md`
- `docs/harness/scope.md`
- <additional docs>

## Acceptance criteria

- <criterion>

## Intended changes

- <file or area>: <change>

## Validation

- <command>: <expected result>

## Risks and rollback

- Risk: <risk>
- Mitigation: <mitigation>
- Rollback: <rollback path>

## Progress log

- <timestamp>: <entry>

## Decisions

- <decision>: <rationale>
""",
        "docs/exec-plans/tech-debt-tracker.md": """
# Technical Debt Tracker

Track recurring drift, stale docs, missing checks, cleanup tasks, and future mechanical enforcement.

| Date | Area | Issue | Proposed cleanup | Status |
| --- | --- | --- | --- | --- |
| <date> | <area> | <issue> | <cleanup> | open |
""",
        "docs/app-specs/index.md": """
# App Specs Index

App specs define user-facing behavior, product intent, and acceptance criteria.

## Docs

- `app-spec.md`: current high-level app spec.

Add more specs here for features, workflows, personas, and product domains.
""",
        "docs/app-specs/app-spec.md": f"""
# App Spec

## Product

{a['project_name']}

## Purpose

{a['purpose']}

## Primary users/operators

{a['users']}

## Product domains/app areas

{md_bullets(a['domains'])}

## User-visible behavior

Document expected workflows, acceptance criteria, and non-goals here.
""",
        "docs/references/index.md": """
# References Index

Place external or copied reference material here so agents can access it without relying on external chat history or inaccessible documents.

## Rules

- Prefer concise, relevant excerpts over huge pasted manuals.
- Record source, date retrieved, and why the reference matters.
- Retire stale references when they no longer reflect the codebase.
""",
        "docs/architecture.md": f"""
# Architecture

## Required boundaries

{md_bullets(a['architecture'])}

## Dependency rules

- Preserve documented layer direction.
- Do not introduce hidden cross-layer coupling.
- Cross-cutting concerns must enter through explicit interfaces.
- Validate data shapes at system boundaries.
- Prefer shared utilities over repeated local helpers when behavior should be consistent.

## Architecture change rule

Architecture changes require an active execution plan and, when listed in `docs/harness/scope.md`, explicit human approval.
""",
        "docs/tooling.md": f"""
# Tooling and Validation

## Tech stack conventions

{md_bullets(a['tech_stack'])}

## Validation commands

{md_bullets(a['commands'])}

## Command reporting

When changing code, report which commands ran, which failed, and which were skipped. Do not invent successful validation.

## Missing command rule

If a relevant validation command is missing, add a note to `docs/exec-plans/tech-debt-tracker.md` or create a plan to add it.
""",
        "docs/quality.md": f"""
# Quality Bar

## Quality invariants

{md_bullets(a['quality'])}

## General expectations

- Keep behavior legible to future agent runs.
- Prefer explicit names and small, testable units.
- Avoid speculative abstractions.
- Do not spread inconsistent patterns.
- Promote repeated review feedback into docs or mechanical checks.
""",
        "docs/security.md": f"""
# Security and Privacy

## Constraints

{md_bullets(a['constraints'])}

## Non-negotiable rules

- Do not weaken authentication, authorization, validation, privacy, or secret handling without explicit harness approval.
- Do not log secrets or sensitive user data.
- Validate untrusted input at boundaries.
- Treat dependency, deployment, and credential changes as approval-required unless scope says otherwise.
""",
        "docs/reliability.md": f"""
# Reliability

## Reliability expectations

{md_bullets(a['constraints'])}

## Operational rules

- Preserve timeouts, retries, idempotency, rate limits, and error handling unless an approved plan says otherwise.
- Do not remove observability needed to diagnose production behavior.
- Prefer deterministic validation over guesswork.
""",
        "docs/observability.md": f"""
# Observability and Agent-Legible Validation

## Workflows

{md_bullets(a['observability'])}

## Agent-legibility goals

- Make local app behavior observable through commands, logs, metrics, traces, screenshots, DOM snapshots, or equivalent tools.
- Document startup and teardown steps.
- Keep validation reproducible per worktree when possible.
""",
        "docs/review.md": """
# Review Expectations

## Local review loop

1. Review the diff before final response.
2. Check that changes stay inside harness scope.
3. Run relevant validation from `docs/tooling.md`.
4. Update docs when durable knowledge changes.
5. Report unresolved risks clearly.

## Feedback loop

When review feedback exposes a reusable rule, update the harness docs or propose a mechanical enforcement check.
""",
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Initialize an agentic coding harness.")
    parser.add_argument("--force", action="store_true", help="overwrite existing generated files")
    parser.add_argument("--non-interactive", action="store_true", help="use defaults or --answers without prompting")
    parser.add_argument("--answers", type=Path, help="JSON file with initialization answers")
    args = parser.parse_args(argv)

    answers = ask_questions(args.non_interactive, args.answers)
    written: list[Path] = []
    skipped: list[Path] = []

    write(ROOT / "AGENTS.md", render_agents(answers), args.force, written, skipped)
    for rel, content in render_docs(answers).items():
        write(ROOT / rel, dedent(content), args.force, written, skipped)

    line_count = len((ROOT / "AGENTS.md").read_text(encoding="utf-8").splitlines()) if (ROOT / "AGENTS.md").exists() else 0

    print("\nHarness initialization complete.")
    print(f"AGENTS.md line count: {line_count}")
    if written:
        print("\nWritten:")
        for path in written:
            print(f"- {path.relative_to(ROOT)}")
    if skipped:
        print("\nSkipped existing files (use --force to overwrite):")
        for path in skipped:
            print(f"- {path.relative_to(ROOT)}")

    if line_count and not (80 <= line_count <= 130):
        print("\nWarning: AGENTS.md is outside the expected ~100-line range.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
