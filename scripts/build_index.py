#!/usr/bin/env python3
"""Validate prompt files and rebuild the prompt index in README.md.

Usage:
    python scripts/build_index.py          # rewrite the index in README.md
    python scripts/build_index.py --check  # fail if files are invalid or the index is stale
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"
REQUIRED_SECTIONS = ("## When to use", "## Prompt")


def parse(path: Path) -> tuple[str, str, list[str]]:
    """Return (title, summary, errors) for one prompt file."""
    text = path.read_text(encoding="utf-8")
    errors = []
    title = re.search(r"^# (.+)$", text, re.M)
    summary = re.search(r"^> (.+)$", text, re.M)
    if not title:
        errors.append("missing '# Title' heading")
    if not summary:
        errors.append("missing '> one-line summary'")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^{re.escape(section)}\s*$", text, re.M):
            errors.append(f"missing '{section}' section")
    if "```text" not in text:
        errors.append("prompt must be inside a ```text code block")
    return (title.group(1).strip() if title else path.stem,
            summary.group(1).strip() if summary else "",
            errors)


def build() -> tuple[str, list[str]]:
    lines, problems = [], []
    for category in sorted(p for p in PROMPTS.iterdir() if p.is_dir()):
        files = sorted(category.glob("*.md"))
        if not files:
            continue
        name = {"devops": "DevOps"}.get(category.name, category.name.capitalize())
        lines += [f"### {name}", "", "| Prompt | What it does |", "| --- | --- |"]
        for f in files:
            title, summary, errors = parse(f)
            rel = f.relative_to(ROOT).as_posix()
            problems += [f"{rel}: {e}" for e in errors]
            lines.append(f"| [{title}]({rel}) | {summary} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", problems


def main() -> int:
    index, problems = build()
    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        problems.append(f"README.md must contain {START} and {END}")
        new_readme = readme
    else:
        head, rest = readme.split(START, 1)
        _, tail = rest.split(END, 1)
        new_readme = f"{head}{START}\n{index}{END}{tail}"

    for p in problems:
        print(f"ERROR: {p}")
    if problems:
        return 1

    if "--check" in sys.argv:
        if new_readme != readme:
            print("ERROR: README index is out of date. Run: python scripts/build_index.py")
            return 1
        print("All prompt files are valid and the index is up to date.")
        return 0

    README.write_text(new_readme, encoding="utf-8")
    print("README index updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
