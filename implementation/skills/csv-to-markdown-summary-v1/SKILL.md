---
name: csv-to-markdown-summary-v1
description: >
  Use when a Task needs to turn an existing CSV file into a readable
  markdown table plus a one-line row/column summary. Reads one CSV,
  writes one markdown file. Does not generate or fabricate data -
  requires a real input CSV already present.
---

# CSV to Markdown Summary (v1)

## What this is

A stdlib-only Python script that reads a CSV file and produces a
markdown file containing a markdown table of its rows and columns,
plus one summary line stating the row and column counts.

## When to use it

Use this Skill whenever a Task has a CSV it needs shown as a readable
markdown table - e.g. turning a data export into something a report or
chat message can display directly. It does not create data; it needs a
real CSV as input.

## Usage

```
python3 csv_to_markdown_summary.py <input.csv> <output.md>
```

Handles ragged rows (padded/truncated to header width) and embedded
`|` characters (escaped) so malformed input can't break the table
structure. Exits 1 with a stderr message if the input file is missing.

## Registered as

`skill-lib/csv-to-markdown-summary-v1`, `status: approved`,
engagements/10-skill-library.md. Retrofitted with this SKILL.md
2026-09-23 to close a packaging gap - the original build produced a
working script and a governance-schema registry entry, but not an
actually-invokable Skill package. No version bump: the underlying
capability and interface are unchanged, only how it's packaged for
discovery.

## Scope

Standard library only (`csv`, `sys`, `pathlib`). No network access, no
third-party dependencies. Reads only the given input path, writes only
the given output path.
