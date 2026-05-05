#!/usr/bin/env python3
"""Validate the structure of a generated agentic coding harness."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

REQUIRED_FILES = [
    "AGENTS.md",
    "docs/README.md",
    "docs/harness/scope.md",
    "docs/harness/initialization.md",
    "docs/harness/operating-model.md",
    "docs/design-docs/index.md",
    "docs/design-docs/core-beliefs.md",
    "docs/exec-plans/index.md",
    "docs/exec-plans/plan-template.md",
    "docs/exec-plans/tech-debt-tracker.md",
    "docs/exec-plans/active/README.md",
    "docs/exec-plans/completed/README.md",
    "docs/app-specs/index.md",
    "docs/app-specs/app-spec.md",
    "docs/references/index.md",
    "docs/architecture.md",
    "docs/tooling.md",
    "docs/quality.md",
    "docs/security.md",
    "docs/reliability.md",
    "docs/observability.md",
    "docs/review.md",
]

SCOPE_REQUIRED_TEXT = [
    "## In scope for coding agents",
    "## Out of scope for coding agents",
    "## Requires explicit human approval",
    "## Scope gate",
    "Harness gate blocked this change.",
]

PLAN_REQUIRED_TEXT = [
    "## Status",
    "## Summary",
    "## Scope",
    "## Harness docs consulted",
    "## Acceptance criteria",
    "## Validation",
    "## Risks and rollback",
    "## Progress log",
    "## Decisions",
]

LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_links(root: Path, failures: list[str]) -> None:
    for path in sorted((root / "docs").rglob("*.md")):
        text = read(path)
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith("<"):
                continue
            if not (path.parent / target).exists():
                failures.append(f"{path.relative_to(root)} has broken relative link: {match.group(1)}")


def check_plan(path: Path, root: Path, failures: list[str]) -> None:
    text = read(path)
    for required in PLAN_REQUIRED_TEXT:
        if required not in text:
            failures.append(f"{path.relative_to(root)} missing required plan section: {required}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate an agentic coding harness.")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    parser.add_argument("--min-agents-lines", type=int, default=80)
    parser.add_argument("--max-agents-lines", type=int, default=130)
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    failures: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            failures.append(f"missing required file: {rel}")

    agents = root / "AGENTS.md"
    if agents.exists():
        line_count = len(read(agents).splitlines())
        if not (args.min_agents_lines <= line_count <= args.max_agents_lines):
            warnings.append(f"AGENTS.md line count is {line_count}, expected {args.min_agents_lines}-{args.max_agents_lines}")
        text = read(agents)
        for required in ["docs/harness/scope.md", "## Scope gate", "Harness gate blocked this change."]:
            if required not in text:
                failures.append(f"AGENTS.md missing required text: {required}")

    scope = root / "docs/harness/scope.md"
    if scope.exists():
        text = read(scope)
        for required in SCOPE_REQUIRED_TEXT:
            if required not in text:
                failures.append(f"docs/harness/scope.md missing required text: {required}")

    tooling = root / "docs/tooling.md"
    if tooling.exists() and "## Validation commands" not in read(tooling):
        failures.append("docs/tooling.md missing validation commands section")

    architecture = root / "docs/architecture.md"
    if architecture.exists() and "## Required boundaries" not in read(architecture):
        failures.append("docs/architecture.md missing required boundaries section")

    for folder in ["docs/exec-plans/active", "docs/exec-plans/completed"]:
        for plan in sorted((root / folder).glob("*.md")):
            if plan.name != "README.md":
                check_plan(plan, root, failures)

    if (root / "docs").exists():
        check_links(root, failures)

    print(f"root: {root}")
    print(f"failures: {len(failures)}")
    print(f"warnings: {len(warnings)}")
    for item in warnings:
        print(f"warning: {item}")
    for item in failures:
        print(f"failure: {item}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
