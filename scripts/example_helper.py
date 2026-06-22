#!/usr/bin/env python3
"""Deterministic prompt section checker.

This helper scans a prompt file for common prompt-engineering sections and
reports missing sections. It does not call external services.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_SECTIONS = [
    "role",
    "goal",
    "context",
    "instructions",
    "constraints",
    "examples",
    "output format",
    "quality check",
]


def normalize(text: str) -> str:
    return " ".join(text.lower().replace("_", " ").replace("-", " ").split())


def check_prompt(text: str) -> dict[str, object]:
    normalized = normalize(text)
    found = [section for section in REQUIRED_SECTIONS if section in normalized]
    missing = [section for section in REQUIRED_SECTIONS if section not in normalized]
    score = round(len(found) / len(REQUIRED_SECTIONS), 2)
    return {
        "score": score,
        "found_sections": found,
        "missing_sections": missing,
        "passes_basic_check": not missing,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a prompt for recommended sections.")
    parser.add_argument("prompt_file", type=Path, help="Path to a text or markdown prompt file.")
    args = parser.parse_args()

    if not args.prompt_file.exists():
        raise SystemExit(f"file not found: {args.prompt_file}")

    result = check_prompt(args.prompt_file.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
