#!/usr/bin/env python3
"""
csv_to_markdown_summary.py

Reads a CSV file and writes a markdown file containing:
  (a) a markdown table of the CSV's rows (header row + data rows), and
  (b) one summary line stating the row count and column count.

Usage:
    python3 csv_to_markdown_summary.py <input.csv> <output.md>

Standard-library only (csv, sys, pathlib). No network access, no
third-party dependencies, no writes outside the given output path.
"""

import csv
import sys
from pathlib import Path


def escape_cell(value: str) -> str:
    """Escape pipe characters and collapse newlines so the cell can't
    break the markdown table's row/column structure."""
    if value is None:
        value = ""
    value = value.replace("|", "\\|")
    value = value.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    return value.strip()


def build_markdown_table(header: list[str], rows: list[list[str]]) -> str:
    lines = []
    lines.append("| " + " | ".join(escape_cell(c) for c in header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    for row in rows:
        # Pad short rows / truncate long rows to match header width so
        # the table stays well-formed even on ragged CSV input.
        padded = list(row) + [""] * (len(header) - len(row))
        padded = padded[: len(header)]
        lines.append("| " + " | ".join(escape_cell(c) for c in padded) + " |")
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python3 csv_to_markdown_summary.py <input.csv> <output.md>",
            file=sys.stderr,
        )
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.is_file():
        print(f"Error: input CSV not found: {input_path}", file=sys.stderr)
        return 1

    with input_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        all_rows = list(reader)

    if not all_rows:
        header: list[str] = []
        data_rows: list[list[str]] = []
    else:
        header = all_rows[0]
        data_rows = all_rows[1:]

    row_count = len(data_rows)
    column_count = len(header)

    table_md = build_markdown_table(header, data_rows) if header else "*(empty CSV - no columns found)*"
    summary_line = f"**Summary:** {row_count} row(s), {column_count} column(s)."

    output_md = f"{table_md}\n\n{summary_line}\n"

    output_path.write_text(output_md, encoding="utf-8")

    print(f"Wrote {output_path} ({row_count} rows, {column_count} columns)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
