#!/usr/bin/env python3
"""Check repository structure and publication boundaries."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
REQUIRED = (
    "PROJECT.md",
    "AGENTS.md",
    "README.md",
    "planning/sequence.md",
    "planning/manuscript-ledger.md",
    "planning/worklist.md",
    "canon/README.md",
    "canon/people.md",
    "canon/places.md",
    "canon/chronology.md",
    "world/README.md",
    "world/place-name-corpus.tsv",
    "publishing/ao3-manifest.yml",
    ".agents/skills/simple-english/SKILL.md",
    ".agents/skills/humanizer/SKILL.md",
    "skills-lock.json",
    "tools/place-names.py",
)
CHAPTER_NAME = re.compile(r"\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
STORYBOARD = re.compile(r"^\[STORYBOARD(?: [a-z0-9-]+)?: .+\]$")


def check():
    problems = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            problems.append(f"missing required file: {relative}")

    for adapter in ("AGENTS.md", "CLAUDE.md"):
        path = ROOT / adapter
        if path.is_file() and "PROJECT.md" not in path.read_text(encoding="utf-8"):
            problems.append(f"agent adapter does not point to PROJECT.md: {adapter}")

    for path in sorted(MANUSCRIPT.glob("*.md")):
        if not CHAPTER_NAME.fullmatch(path.name):
            problems.append(f"invalid chapter filename: {path.relative_to(ROOT)}")
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "[STORYBOARD" in line and not STORYBOARD.fullmatch(line):
                problems.append(
                    f"invalid storyboard syntax: {path.relative_to(ROOT)}:{number}"
                )
            if line.startswith("//"):
                problems.append(
                    f"use <!-- --> for author notes: {path.relative_to(ROOT)}:{number}"
                )

    for path in ROOT.rglob("*.dup-bak"):
        if ".git" not in path.parts:
            problems.append(f"duplicate backup file: {path.relative_to(ROOT)}")

    if (ROOT / "notes").exists():
        problems.append("retired notes/ directory is present")

    for obsolete in (
        "tools/ao3-chapters.tsv",
        "ao3-chapters.json",
        "canon/pedigree.dot",
        "canon/setting-map.dot",
    ):
        if (ROOT / obsolete).exists():
            problems.append(f"obsolete duplicate is present: {obsolete}")

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    print("project checks: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
