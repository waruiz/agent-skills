#!/usr/bin/env python3
"""Validate the shape and token discipline of a generated project context brief."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


MARKER = "<!-- PROJECT_CONTEXT_MAINTENANCE_V1 -->"
REQUIRED_HEADINGS = (
    "## Project in one minute",
    "## Boundaries",
    "## Invariants and accepted decisions",
    "## Architecture and primary flow",
    "## Contracts and durable state",
    "## Repository and operations",
    "## Delivery map",
    "## Open decisions and risks",
    "## Durable clarifications",
    "## Starting a ticket",
    "## Context maintenance marker",
    "## Sources",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--max-words", type=int, default=1800)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    if args.max_words < 1:
        print("ERROR: --max-words must be positive", file=sys.stderr)
        return 2
    if not args.document.is_file():
        print(f"ERROR: document not found: {args.document}", file=sys.stderr)
        return 2

    text = args.document.read_text(encoding="utf-8")
    marker_count = text.count(MARKER)
    if marker_count != 1:
        errors.append(f"maintenance marker must appear exactly once (found {marker_count})")

    for heading in REQUIRED_HEADINGS:
        count = text.count(heading)
        if count != 1:
            errors.append(f"required heading must appear exactly once: {heading!r} (found {count})")

    placeholders = sorted(set(re.findall(r"\{\{[^{}]+\}\}", text)))
    if placeholders:
        errors.append("unresolved template placeholders: " + ", ".join(placeholders))

    word_count = len(re.findall(r"\b[\w'-]+\b", text))
    if word_count > args.max_words:
        errors.append(f"word count {word_count} exceeds ceiling {args.max_words}")

    if not re.search(r"^#\s+.+\s+—\s+Agent Context\s*$", text, re.MULTILINE):
        errors.append("first-level title must end with '— Agent Context'")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.document} ({word_count} words, marker present, required sections present)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
