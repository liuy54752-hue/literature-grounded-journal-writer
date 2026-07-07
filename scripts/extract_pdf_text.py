#!/usr/bin/env python3
"""Extract PDF text with page labels when pypdf or PyPDF2 is available."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def load_reader():
    try:
        from pypdf import PdfReader  # type: ignore

        return PdfReader
    except Exception:
        try:
            from PyPDF2 import PdfReader  # type: ignore

            return PdfReader
        except Exception as exc:
            raise RuntimeError(
                "Install pypdf or PyPDF2 to use this script: python3 -m pip install pypdf"
            ) from exc


def extract_pdf(pdf_path: Path) -> str:
    reader_cls = load_reader()
    reader = reader_cls(str(pdf_path))
    chunks: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n=== Page {index} ===\n{text.strip()}")
    return "\n".join(chunks).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF while preserving page boundaries."
    )
    parser.add_argument("pdf", type=Path, help="Input PDF path")
    parser.add_argument(
        "-o", "--output", type=Path, help="Optional output text file. Defaults to stdout."
    )
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    try:
        text = extract_pdf(args.pdf)
    except Exception as exc:
        print(f"Failed to extract PDF text: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
