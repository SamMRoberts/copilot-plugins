#!/usr/bin/env python3
"""Inspect section-state markdown files for an agentic coding harness."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys

DEFAULT_SECTIONS = [
    "harness_purpose",
    "supported_work",
    "out_of_scope",
    "required_context",
    "knowledge_system",
    "operating_phases",
    "boundaries",
    "agent_legibility",
    "mechanical_enforcement",
    "verification_gates",
    "evidence_requirements",
    "handoff_format",
    "automation_plan",
    "feedback_loops",
    "open_questions",
]

STATES = {"complete", "needs_update", "failed"}
PATTERN = re.compile(r"^(?P<section>[a-z0-9_]+)\.(?P<state>complete|needs_update|failed)\.md$")


@dataclass(frozen=True)
class SectionFile:
    section: str
    state: str
    path: Path


@dataclass(frozen=True)
class SectionStatus:
    section: str
    state: str
    path: str | None
    action: str
    note: str


def normalize_section(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = normalized.strip("_")
    normalized = re.sub(r"_{2,}", "_", normalized)
    if not normalized:
        raise ValueError(f"Invalid empty section name from {value!r}")
    return normalized


def parse_sections(raw: str | None) -> list[str]:
    if not raw:
        return DEFAULT_SECTIONS
    sections = [normalize_section(item) for item in raw.split(",") if item.strip()]
    if len(set(sections)) != len(sections):
        raise ValueError("Section list contains duplicates after normalization.")
    return sections or DEFAULT_SECTIONS


def collect_files(directory: Path) -> tuple[list[SectionFile], list[Path]]:
    section_files: list[SectionFile] = []
    ignored: list[Path] = []
    if not directory.exists():
        return section_files, ignored
    for path in sorted(directory.glob("*.md")):
        match = PATTERN.match(path.name)
        if not match:
            ignored.append(path)
            continue
        section_files.append(SectionFile(match.group("section"), match.group("state"), path))
    return section_files, ignored


def classify_sections(directory: Path, required: list[str]) -> list[SectionStatus]:
    files, _ = collect_files(directory)
    by_section: dict[str, list[SectionFile]] = {}
    for item in files:
        by_section.setdefault(item.section, []).append(item)

    statuses: list[SectionStatus] = []
    for section in required:
        matches = by_section.get(section, [])
        if not matches:
            statuses.append(
                SectionStatus(
                    section=section,
                    state="failed",
                    path=None,
                    action="create_from_scratch",
                    note="No state file exists for this section.",
                )
            )
            continue

        if len(matches) > 1:
            paths = ", ".join(str(item.path) for item in matches)
            statuses.append(
                SectionStatus(
                    section=section,
                    state="failed",
                    path=None,
                    action="resolve_state_conflict",
                    note=f"Multiple state files exist for this section: {paths}",
                )
            )
            continue

        item = matches[0]
        if item.state == "complete":
            action = "skip"
            note = "Section is complete."
        elif item.state == "needs_update":
            action = "improve_existing"
            note = "Use the current content as the starting point and improve it."
        else:
            action = "regenerate_from_scratch"
            note = "Discard this section's content and create a new version."
        statuses.append(SectionStatus(item.section, item.state, str(item.path), action, note))

    return statuses


def init_missing_files(directory: Path, statuses: list[SectionStatus]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for status in statuses:
        if status.path is not None:
            continue
        path = directory / f"{status.section}.failed.md"
        path.write_text(
            "\n".join(
                [
                    f"# {status.section}",
                    "",
                    "State: failed",
                    "",
                    "This section has not been drafted yet. Regenerate it from scratch.",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def choose_next(statuses: list[SectionStatus]) -> SectionStatus | None:
    for status in statuses:
        if status.action in {"resolve_state_conflict", "regenerate_from_scratch", "create_from_scratch"}:
            return status
    for status in statuses:
        if status.action == "improve_existing":
            return status
    return None


def to_payload(directory: Path, required: list[str], statuses: list[SectionStatus], ignored: list[Path]) -> dict:
    next_status = choose_next(statuses)
    counts = {state: 0 for state in sorted(STATES)}
    for status in statuses:
        counts[status.state] += 1
    return {
        "directory": str(directory),
        "required_sections": len(required),
        "complete": counts["complete"],
        "needs_update": counts["needs_update"],
        "failed": counts["failed"],
        "ignored_files": [str(path) for path in ignored],
        "all_complete": next_status is None,
        "next": None if next_status is None else next_status.__dict__,
        "sections": [status.__dict__ for status in statuses],
    }


def print_text(payload: dict) -> None:
    print(f"directory: {payload['directory']}")
    print(f"required_sections: {payload['required_sections']}")
    print(f"complete: {payload['complete']}")
    print(f"needs_update: {payload['needs_update']}")
    print(f"failed: {payload['failed']}")
    print(f"ignored_files: {len(payload['ignored_files'])}")
    if payload["next"]:
        print(f"next_action: {payload['next']['action']}")
        print(f"section: {payload['next']['section']}")
        if payload["next"]["path"]:
            print(f"file: {payload['next']['path']}")
        print(f"note: {payload['next']['note']}")
    else:
        print("next_action: skip")
        print("status: all required sections complete")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Report next harness section validation action.")
    parser.add_argument("--dir", default=".harness-validation", help="validation directory")
    parser.add_argument("--sections", help="comma-separated required section list")
    parser.add_argument("--init-missing", action="store_true", help="create missing section files as <section>.failed.md")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args(argv)

    directory = Path(args.dir)
    required = parse_sections(args.sections)
    statuses = classify_sections(directory, required)
    if args.init_missing:
        init_missing_files(directory, statuses)
        statuses = classify_sections(directory, required)
    _, ignored = collect_files(directory)
    payload = to_payload(directory, required, statuses, ignored)

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_text(payload)

    return 0 if payload["all_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
