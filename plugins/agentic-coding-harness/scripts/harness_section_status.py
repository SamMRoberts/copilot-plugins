#!/usr/bin/env python3
"""Inspect section-state markdown files for an agentic coding harness."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


STATES = ("complete", "needs_update", "failed")
DEFAULT_SECTIONS = (
    "harness_purpose",
    "supported_work",
    "out_of_scope",
    "required_context",
    "operating_phases",
    "boundaries",
    "verification_gates",
    "evidence_requirements",
    "handoff_format",
    "automation_plan",
    "open_questions",
)


@dataclass
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


def parse_sections(raw_sections: str | None) -> tuple[str, ...]:
    if not raw_sections:
        return DEFAULT_SECTIONS
    sections = tuple(normalize_section(section) for section in raw_sections.split(","))
    if len(set(sections)) != len(sections):
        raise ValueError("Section list contains duplicates after normalization.")
    return sections


def find_state_files(validation_dir: Path, section: str) -> list[tuple[str, Path]]:
    matches: list[tuple[str, Path]] = []
    for state in STATES:
        path = validation_dir / f"{section}.{state}.md"
        if path.exists():
            matches.append((state, path))
    return matches


def classify_section(validation_dir: Path, section: str) -> SectionStatus:
    matches = find_state_files(validation_dir, section)

    if not matches:
        return SectionStatus(
            section=section,
            state="failed",
            path=None,
            action="create_from_scratch",
            note="No state file exists for this section.",
        )

    if len(matches) > 1:
        paths = ", ".join(str(path) for _, path in matches)
        return SectionStatus(
            section=section,
            state="failed",
            path=None,
            action="resolve_state_conflict",
            note=f"Multiple state files exist for this section: {paths}",
        )

    state, path = matches[0]
    if state == "complete":
        action = "skip"
        note = "Section is complete."
    elif state == "needs_update":
        action = "improve_existing"
        note = "Use the current content as the starting point and improve it."
    else:
        action = "regenerate_from_scratch"
        note = "Discard this section's content and create a new version."

    return SectionStatus(
        section=section,
        state=state,
        path=str(path),
        action=action,
        note=note,
    )


def init_missing_files(validation_dir: Path, statuses: list[SectionStatus]) -> None:
    validation_dir.mkdir(parents=True, exist_ok=True)
    for status in statuses:
        if status.path is not None:
            continue
        path = validation_dir / f"{status.section}.failed.md"
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
        if status.action in {"regenerate_from_scratch", "create_from_scratch", "resolve_state_conflict"}:
            return status
    for status in statuses:
        if status.action == "improve_existing":
            return status
    return None


def to_payload(statuses: list[SectionStatus]) -> dict:
    next_status = choose_next(statuses)
    return {
        "all_complete": next_status is None,
        "next": None if next_status is None else next_status.__dict__,
        "sections": [status.__dict__ for status in statuses],
    }


def print_markdown(payload: dict) -> None:
    if payload["all_complete"]:
        print("# Harness Section Status")
        print()
        print("All sections are complete.")
        return

    next_status = payload["next"]
    print("# Harness Section Status")
    print()
    print("## Next Action")
    print()
    print(f"- Section: `{next_status['section']}`")
    print(f"- State: `{next_status['state']}`")
    print(f"- Action: `{next_status['action']}`")
    if next_status["path"]:
        print(f"- File: `{next_status['path']}`")
    print(f"- Note: {next_status['note']}")
    print()
    print("## Sections")
    print()
    for status in payload["sections"]:
        path = status["path"] or "[missing]"
        print(f"- `{status['section']}`: `{status['state']}` -> `{status['action']}` ({path})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect <section>.<state>.md files and report the next harness refinement action."
    )
    parser.add_argument(
        "--dir",
        default=".harness-validation",
        help="Directory containing section-state markdown files.",
    )
    parser.add_argument(
        "--sections",
        help="Comma-separated section names. Defaults to the standard harness sections.",
    )
    parser.add_argument(
        "--init-missing",
        action="store_true",
        help="Create missing section files as <section>.failed.md.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of markdown.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validation_dir = Path(args.dir)
    sections = parse_sections(args.sections)
    statuses = [classify_section(validation_dir, section) for section in sections]

    if args.init_missing:
        init_missing_files(validation_dir, statuses)
        statuses = [classify_section(validation_dir, section) for section in sections]

    payload = to_payload(statuses)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_markdown(payload)

    return 0 if payload["all_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
