"""Write the repository's folder tree into README.md between marker comments.

Usage:
    python .github/scripts/update_readme_tree.py          # rewrite README.md
    python .github/scripts/update_readme_tree.py --check  # report only; exit 1 if stale
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
START = "<!-- tree:start -->"
END = "<!-- tree:end -->"

# Dotfiles and tooling folders are repo plumbing, not part of what a reader
# downloads, so they stay out of the tree.
SKIP_PREFIX = "."

# Comments are matched by name so a newly added assessment is annotated
# without editing this script.


def comment_for(path: Path) -> str:
    if path.is_dir() and path.name == "data":
        return "Data (.csv.gz)"
    if path.suffix == ".html":
        return "Instructions"
    if path.suffix == ".xlsx":
        return "Data"
    if path.name.endswith("_answer_key.md"):
        return "Answer key"
    if path.name == "reference_solution.py":
        return "Reproduces the answer key"
    return ""


def children(folder: Path) -> list[Path]:
    # Collapse the contents of data/ folders: the file names are listed in
    # each assessment's instructions, and listing them here doubles the tree.
    if folder.name == "data":
        return []
    entries = [p for p in folder.iterdir() if not p.name.startswith(SKIP_PREFIX)]
    return sorted(entries, key=lambda p: p.name.casefold())


def render(folder: Path, prefix: str = "") -> list[tuple[str, str]]:
    rows = []
    items = children(folder)
    for i, item in enumerate(items):
        last = i == len(items) - 1
        name = item.name + ("/" if item.is_dir() else "")
        rows.append((f"{prefix}{'└── ' if last else '├── '}{name}", comment_for(item)))
        if item.is_dir():
            rows.extend(render(item, prefix + ("    " if last else "│   ")))
    return rows


def build_block() -> str:
    rows = [(f"{ROOT.name}/", ""), *render(ROOT)]
    # Align comments two spaces past the longest line so they form one column
    # however long a new assessment's file names are.
    col = max(len(line) for line, _ in rows) + 2
    tree = "\n".join(f"{line.ljust(col)}# {note}" if note else line for line, note in rows)
    return f"{START}\n```\n{tree}\n```\n{END}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report only; exit 1 if the tree is out of date")
    args = parser.parse_args()

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print(f"README.md needs both {START} and {END} markers.", file=sys.stderr)
        return 2

    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = head + build_block() + tail

    if updated == text:
        print("Project tree is up to date.")
        return 0
    if args.check:
        print("Project tree is out of date. Run without --check to update it.")
        return 1
    README.write_text(updated, encoding="utf-8")
    print("Updated the project tree in README.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
