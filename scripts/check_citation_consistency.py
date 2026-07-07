#!/usr/bin/env python3
"""Lightweight citation consistency check for draft text and references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


IN_TEXT = re.compile(r"\(([A-Z][A-Za-z'\-]+(?:\s+et al\.)?,\s*(?:19|20)\d{2}[a-z]?)\)")
REF_START = re.compile(r"^([A-Z][A-Za-z'\-]+).*?\b((?:19|20)\d{2}[a-z]?)\b")


def normalize_author(author: str) -> str:
    return author.replace(" et al.", "").strip().lower()


def collect_in_text(text: str) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for match in IN_TEXT.finditer(text):
        content = match.group(1)
        author, year = [part.strip() for part in content.rsplit(",", 1)]
        pairs.add((normalize_author(author), year.lower()))
    return pairs


def collect_references(text: str) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for line in text.splitlines():
        match = REF_START.search(line.strip())
        if match:
            pairs.add((normalize_author(match.group(1)), match.group(2).lower()))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare simple author-year in-text citations with a reference list."
    )
    parser.add_argument("draft", type=Path, help="Draft manuscript text file")
    parser.add_argument("references", type=Path, help="Reference list text file")
    args = parser.parse_args()

    draft = args.draft.read_text(encoding="utf-8")
    references = args.references.read_text(encoding="utf-8")

    cited = collect_in_text(draft)
    listed = collect_references(references)

    missing = sorted(cited - listed)
    unused = sorted(listed - cited)

    print("Citation consistency report")
    print("===========================")
    print(f"In-text citation pairs: {len(cited)}")
    print(f"Reference-list pairs: {len(listed)}")

    if missing:
        print("\nCited in text but not found in references:")
        for author, year in missing:
            print(f"- {author}, {year}")
    else:
        print("\nNo missing reference-list matches detected.")

    if unused:
        print("\nIn references but not detected in text:")
        for author, year in unused:
            print(f"- {author}, {year}")
    else:
        print("\nNo unused reference-list entries detected.")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
