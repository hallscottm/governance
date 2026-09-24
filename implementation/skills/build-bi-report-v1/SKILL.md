---
name: build-bi-report-v1
description: >
  Use when a Task needs an HTML Report/Dashboard built from an
  already-existing, already-produced weekly data-quality-metrics CSV
  (one row per check_name, table_name, week_ending, with pass_count,
  fail_count, pass_rate - the shape produced by
  dq-metrics-dummy-data-generator-v1 or an equivalent real export).
  Renders a self-contained, dependency-free HTML dashboard: a line
  chart of weekly pass rate per check/table pair, a latest-week status
  table, and summary stat tiles. Do not use this to author, run, or
  evaluate a new Data Quality Rule - it only visualizes metrics that
  already exist. Internal-distribution, non-Confidential data only:
  this Skill does not implement Certified-status badging (BIPOL-1/2)
  or Row-Level Security (BIPOL-3) - do not point it at Confidential/
  Restricted/PII sources.
status: approved
---

# Build BI Report (v1)

## What this is

A stdlib-only Python script (`build_bi_report.py`) that reads a weekly
data-quality-metrics CSV and writes a single, self-contained HTML file:
a line chart (weekly pass rate per `(check_name, table_name)` pair,
with a legend and hover tooltip), a latest-week status table (sorted
worst pass rate first, with a status pill per row), and summary stat
tiles (pair count, weeks covered, overall latest-week pass rate, pairs
below the warn threshold, and the worst-performing pair). The chart and
table are rendered client-side by inline JS/SVG/CSS from a JSON payload
the Python script embeds in the page - no build step, no external
scripts, fonts, or stylesheets, and it opens standalone, offline, in
any modern browser.

## When to use it

Use this Skill whenever a Task needs a BI dashboard built from an
already-produced metrics CSV shaped like
`check_name,table_name,week_ending,pass_count,fail_count,pass_rate`
(e.g. the output of `dq-metrics-dummy-data-generator-v1`, or a real
data-quality-checks export in the same shape).

Do NOT use this Skill to:
- Author, run, or evaluate a Data Quality Rule - it has no rule-checking
  logic at all; it only visualizes a metrics CSV that already exists.
- Produce a report for Organization-wide or External distribution. Its
  output always renders as an uncertified/Draft-status report (see
  Scope below) - Certification is a separate, human-driven process this
  Skill does not perform.
- Report on Confidential, Restricted, or PII-containing data. It has no
  Row-Level Security or access-control mechanism of any kind; every row
  of the input CSV is visible in the output HTML to anyone who opens it.

## Usage

```
python3 build_bi_report.py <input.csv> <output.html> \
    --refresh-schedule "Weekly, Mondays 06:00 UTC" \
    [--title "Weekly Data Quality Dashboard"] \
    [--distribution-scope Internal|Departmental] \
    [--warn-threshold 0.95] [--critical-threshold 0.80] \
    [--source-note "some description of the source extract"]
```

**Positional arguments**
- `input` - path to the source CSV. Must have a header row with (at
  least) the columns `check_name, table_name, week_ending, pass_count,
  fail_count, pass_rate`. `week_ending` must be an ISO `YYYY-MM-DD`
  date; `pass_count`/`fail_count` must be non-negative integers;
  `pass_rate` must be a float in `[0, 1]`.
- `output` - path to write the generated HTML dashboard to.

**Required flag**
- `--refresh-schedule TEXT` - the declared Report Refresh Schedule
  (BIPOL-4). The script will not guess or default this: an extract with
  no declared refresh cadence has undefined staleness, and this script
  has no way to know the real operational cadence of the upstream
  export. The caller (the Task/Skill invoking this one, or a human)
  must supply the real cadence.

**Optional flags**
- `--title TEXT` - dashboard page title (default: `Weekly Data Quality
  Dashboard`).
- `--distribution-scope {Internal,Departmental}` - rendered in the
  output's banner and scope note (default: `Internal`). Only these two
  values are accepted; Organization-wide/External are refused by
  `argparse`'s `choices` because this Skill's output is never Certified
  (see Scope below) and BIPOL-1 requires Certified status before either
  of those scopes is reachable.
- `--warn-threshold FLOAT` (default `0.95`) / `--critical-threshold
  FLOAT` (default `0.80`) - latest-week status-pill thresholds. A
  pair's latest-week pass rate `>= warn-threshold` is "On Target",
  `>= critical-threshold` (but below warn) is "Warning", below
  `critical-threshold` is "Critical". Must satisfy `0 <=
  critical-threshold <= warn-threshold <= 1`.
- `--source-note TEXT` - short description of the source extract shown
  in the footer (default: the input file's name).

**Exit codes:** `0` on success; `2` on invalid arguments or a
structurally invalid input CSV (missing required column, unparseable
date/number, `pass_rate` outside `[0, 1]`, or no data rows) - the error
message names the specific problem and, for a bad row, its line number.

## What the output looks like

A single HTML file (no separate assets) with:
- A banner naming the pair count, week count, week range, and
  distribution scope.
- A **Scope** note stating the report is Internal/Departmental-only,
  uncertified, and has no Row-Level Security.
- A **Refresh schedule** line carrying the `--refresh-schedule` text
  and generation timestamp (BIPOL-4).
- Stat tiles: pair count, weeks covered, latest-week overall pass rate
  (volume-weighted across pairs), pairs below the warn threshold (with
  the critical count as a sub-line), and the worst-performing pair.
- A line chart, one series per `(check_name, table_name)` pair, with a
  clickable legend (click to isolate/restore a series) and a hover
  tooltip showing every visible series' value for the nearest week.
- A latest-week status table, sorted worst-pass-rate-first, with a
  status pill (`On Target` / `Warning` / `Critical` / `No Data`) per
  row. A pair with no row for the latest week (sparse/late-arriving
  data) shows `No Data` rather than being silently dropped.

## Scope

**Internal-distribution, non-Confidential data only.** This Skill's
output must satisfy 06-bi-reporting/06-policies.md's BIPOL-4
(Data Extract Refresh Schedule Required) unconditionally, which it
does (see the required `--refresh-schedule` flag above). It does
**not** implement, and its output does not claim:
- **BIPOL-1/BIPOL-2 (Certified Status)** - the output always renders as
  an uncertified report and `--distribution-scope` refuses anything
  beyond Internal/Departmental. Getting a report built by this Skill to
  Certified status (and clearing it for Organization-wide/External
  distribution) is a separate, human-reviewed process this Skill plays
  no part in.
- **BIPOL-3/BIAR-2 (Row-Level Security)** - there is no row-filtering,
  masking, or access-control logic anywhere in this script. Every row
  of the input CSV appears in the output HTML, visible to anyone who
  can open the file. Do not run this Skill against a source whose
  Sensitivity Level is Confidential or Restricted, or that Contains PII
  - those require Row-Level Security (BIPOL-3) that this Skill was not
  asked to, and does not, provide.

Standard library only (`argparse`, `csv`, `json`, `datetime`, `pathlib`,
`html`, `sys`). No network access, no third-party dependencies, and no
writes outside the single `output` path given on the command line. The
generated HTML page itself uses only browser-native SVG/CSS/JS - no
external scripts, fonts, or stylesheets - so it renders standalone and
offline.

## Eval fixtures

See `eval/` alongside this Skill in the Factory Run's Sandbox for three
test CSVs (and the HTML each produces): `eval_normal.csv` (three
healthy pairs, no low-pass weeks), `eval_bad_week.csv` (a pair whose
latest week drops sharply to ~49% pass rate, exercising the "Critical"
status pill and the worst-pair tile), and `eval_single_week.csv` (two
pairs with only one `week_ending` each, exercising the single-data-
point chart/table path).
