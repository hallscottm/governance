#!/usr/bin/env python3
"""
build_bi_report.py

skill-lib/build-bi-report-v1

Assembles a self-contained HTML Report/Dashboard from an already-existing,
already-produced weekly data-quality-metrics CSV (the shape produced by
the dq-metrics-dummy-data-generator-v1 Skill, or an equivalent real
export): one row per (check_name, table_name, week_ending), columns:

    check_name, table_name, week_ending, pass_count, fail_count, pass_rate

This Skill does NOT author, run, or evaluate any Data Quality Rule. It
only reads an already-computed metrics CSV and renders it as a
dashboard: a line chart of weekly pass rate per (check, table) pair, a
latest-week status table, and summary stat tiles.

Scope (read this before using the output for anything beyond a pilot):

  - Internal-distribution, non-Confidential data only. This Skill does
    not implement, and its output does not claim, any of the following:
      * Certified Report/Dashboard status (06-bi-reporting/06-policies.md
        BIPOL-1, BIPOL-2) - the output always renders as an uncertified/
        Draft-status report. Certifying it (and clearing it for
        Organization-wide or External Distribution Scope) is a separate,
        human-driven process this Skill does not perform.
      * Row-Level Security (BIPOL-3) - do not point this Skill at a data
        source whose Sensitivity Level is Confidential or Restricted, or
        that Contains PII. It has no access-control or row-filtering
        logic of any kind; every row in the input CSV appears in the
        output, visible to anyone who opens the HTML file.
  - The one BI policy this Skill DOES apply unconditionally is BIPOL-4
    (Data Extract Refresh Schedule Required): the output always renders
    a declared Report Refresh Schedule note, because the CSV it reads is
    itself a static data extract with no live connection. The refresh
    schedule text is supplied by the caller (--refresh-schedule); this
    script has no way to know the real operational cadence of the
    upstream export and will not guess one silently - the flag is
    required.

Standard library only (argparse, csv, json, statistics, datetime,
pathlib, html). No network access, no third-party dependencies, no
writes outside the single --output path given on the command line. The
generated HTML page itself uses only browser-native SVG/CSS/JS (no
external scripts, fonts, or stylesheets) so it opens standalone, offline,
in any modern browser.

Usage:
    python3 build_bi_report.py <input.csv> <output.html> \\
        --refresh-schedule "Weekly, Mondays 06:00 UTC" \\
        --title "Weekly Data Quality Dashboard" \\
        --warn-threshold 0.95 --critical-threshold 0.80

Exit codes: 0 on success, 2 on invalid arguments or malformed input CSV.
"""

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path

REQUIRED_COLUMNS = ["check_name", "table_name", "week_ending", "pass_count", "fail_count", "pass_rate"]


def read_rows(input_path: Path):
    """Read and validate the input CSV. Returns a list of normalized dict
    rows, or raises ValueError with a human-readable message on any
    structural problem (missing columns, unparseable numbers, etc.)."""
    with input_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("input CSV has no header row")
        missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing:
            raise ValueError(
                f"input CSV is missing required column(s): {', '.join(missing)} "
                f"(found: {', '.join(reader.fieldnames)})"
            )

        rows = []
        for i, raw in enumerate(reader, start=2):  # start=2: header is line 1
            try:
                week = raw["week_ending"].strip()
                if not week:
                    raise ValueError("empty week_ending")
                # Validate it's an ISO date without pulling in a heavier parser.
                datetime.strptime(week, "%Y-%m-%d")

                pass_count = int(raw["pass_count"])
                fail_count = int(raw["fail_count"])
                pass_rate = float(raw["pass_rate"])

                if pass_count < 0 or fail_count < 0:
                    raise ValueError("pass_count/fail_count must be >= 0")
                if not (0.0 <= pass_rate <= 1.0):
                    raise ValueError("pass_rate must be between 0 and 1")

                rows.append(
                    {
                        "check_name": raw["check_name"].strip(),
                        "table_name": raw["table_name"].strip(),
                        "week_ending": week,
                        "pass_count": pass_count,
                        "fail_count": fail_count,
                        "pass_rate": pass_rate,
                    }
                )
            except (ValueError, KeyError) as e:
                raise ValueError(f"input CSV row {i}: {e}") from e

        if not rows:
            raise ValueError("input CSV has a header but no data rows")

        return rows


def pair_key(row):
    return (row["check_name"], row["table_name"])


def pair_label(row):
    return f"{row['check_name']} / {row['table_name']}"


def status_of(pass_rate, warn_threshold, critical_threshold):
    """Three-tier status, consistent in spirit with the existing
    dq_dashboard.html pilot's status pill convention, but with two
    caller-configurable thresholds instead of a fixed four-tier scale -
    this Skill does not know the right tier count for every consumer's
    data, so it keeps the model simple and adjustable."""
    if pass_rate >= warn_threshold:
        return "good"
    if pass_rate >= critical_threshold:
        return "warning"
    return "critical"


def build_dashboard_data(rows, warn_threshold, critical_threshold):
    """Turn the flat row list into the structures the HTML template's
    embedded JS needs: sorted weeks, sorted pairs (each with its own
    week-ordered series), and a latest-week status table."""
    weeks = sorted({r["week_ending"] for r in rows})
    latest_week = weeks[-1]

    pairs = {}
    for r in rows:
        pairs.setdefault(pair_key(r), []).append(r)
    for k in pairs:
        pairs[k].sort(key=lambda r: r["week_ending"])

    # Stable, readable ordering: worst latest-week pass rate first (the
    # rows most likely to need attention), pairs with no latest-week row
    # last.
    def latest_rate_for_sort(k):
        for r in pairs[k]:
            if r["week_ending"] == latest_week:
                return r["pass_rate"]
        return 2.0  # sorts after every real rate

    sorted_pair_keys = sorted(pairs.keys(), key=latest_rate_for_sort)

    series = []
    for k in sorted_pair_keys:
        series.append(
            {
                "check_name": k[0],
                "table_name": k[1],
                "label": f"{k[0]} / {k[1]}",
                "points": [{"week": r["week_ending"], "pass_rate": r["pass_rate"]} for r in pairs[k]],
            }
        )

    latest_table = []
    for k in sorted_pair_keys:
        row = next((r for r in pairs[k] if r["week_ending"] == latest_week), None)
        if row is None:
            latest_table.append(
                {
                    "check_name": k[0],
                    "table_name": k[1],
                    "pass_count": None,
                    "fail_count": None,
                    "pass_rate": None,
                    "status": "no_data",
                }
            )
        else:
            latest_table.append(
                {
                    "check_name": k[0],
                    "table_name": k[1],
                    "pass_count": row["pass_count"],
                    "fail_count": row["fail_count"],
                    "pass_rate": row["pass_rate"],
                    "status": status_of(row["pass_rate"], warn_threshold, critical_threshold),
                }
            )

    latest_rows = [r for r in rows if r["week_ending"] == latest_week]
    total_pass = sum(r["pass_count"] for r in latest_rows)
    total_fail = sum(r["fail_count"] for r in latest_rows)
    total_checked = total_pass + total_fail
    overall_latest_rate = (total_pass / total_checked) if total_checked > 0 else None

    below_warn = sum(1 for r in latest_table if r["status"] in ("warning", "critical"))
    critical_count = sum(1 for r in latest_table if r["status"] == "critical")

    worst = None
    worst_rate = None
    for r in latest_table:
        if r["pass_rate"] is None:
            continue
        if worst_rate is None or r["pass_rate"] < worst_rate:
            worst_rate = r["pass_rate"]
            worst = r

    tiles = {
        "pair_count": len(sorted_pair_keys),
        "week_count": len(weeks),
        "week_range": f"{weeks[0]} through {weeks[-1]}",
        "latest_week": latest_week,
        "overall_latest_rate": overall_latest_rate,
        "below_warn_count": below_warn,
        "critical_count": critical_count,
        "worst_pair_label": (f"{worst['check_name']} / {worst['table_name']}" if worst else None),
        "worst_pair_rate": worst_rate,
    }

    return {
        "weeks": weeks,
        "series": series,
        "latest_table": latest_table,
        "tiles": tiles,
        "warn_threshold": warn_threshold,
        "critical_threshold": critical_threshold,
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{ color-scheme: light; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; padding: 0; }}
  body {{
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: #f9f9f7;
    color: #0b0b0b;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{ color-scheme: dark; }}
    body:where(:not([data-theme="light"] body)) {{ background: #0d0d0d; color: #ffffff; }}
  }}
  :root[data-theme="dark"] body {{ background: #0d0d0d; color: #ffffff; }}

  .viz-root {{
    --surface-1: #fcfcfb;
    --page-plane: #f9f9f7;
    --text-primary: #0b0b0b;
    --text-secondary: #52514e;
    --text-muted: #898781;
    --gridline: #e1e0d9;
    --baseline: #c3c2b7;
    --border: rgba(11,11,11,0.10);
    --good: #0ca30c;
    --warning: #fab219;
    --critical: #d03b3b;
    --series-1: #2a78d6;
    --series-2: #eb6834;
    --series-3: #1baf7a;
    --series-4: #eda100;
    --series-5: #e87ba4;
    --series-6: #008300;
    --series-7: #8862d6;
    --series-8: #4aa9c9;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) .viz-root {{
      --surface-1: #1a1a19;
      --page-plane: #0d0d0d;
      --text-primary: #ffffff;
      --text-secondary: #c3c2b7;
      --text-muted: #898781;
      --gridline: #2c2c2a;
      --baseline: #383835;
      --border: rgba(255,255,255,0.10);
      --good: #0ca30c;
      --warning: #fab219;
      --critical: #e66767;
      --series-1: #3987e5;
      --series-2: #d95926;
      --series-3: #199e70;
      --series-4: #c98500;
      --series-5: #d55181;
      --series-6: #008300;
      --series-7: #a186e0;
      --series-8: #6cc0dd;
    }}
  }}
  :root[data-theme="dark"] .viz-root {{
    --surface-1: #1a1a19;
    --page-plane: #0d0d0d;
    --text-primary: #ffffff;
    --text-secondary: #c3c2b7;
    --text-muted: #898781;
    --gridline: #2c2c2a;
    --baseline: #383835;
    --border: rgba(255,255,255,0.10);
    --series-1: #3987e5;
    --series-2: #d95926;
    --series-3: #199e70;
    --series-4: #c98500;
    --series-5: #d55181;
    --series-6: #008300;
    --series-7: #a186e0;
    --series-8: #6cc0dd;
  }}

  .viz-root {{ max-width: 980px; margin: 0 auto; padding: 24px 16px 48px; background: var(--page-plane); }}
  .banner h1 {{ font-size: 1.4rem; margin: 0 0 4px; }}
  .banner .sub {{ color: var(--text-secondary); font-size: 0.9rem; margin: 0 0 4px; }}
  .scope-note {{
    font-size: 0.82rem; color: var(--text-muted); border: 1px solid var(--border);
    border-radius: 8px; padding: 8px 12px; margin: 10px 0 18px; background: var(--surface-1);
  }}
  .refresh-note {{
    font-size: 0.82rem; color: var(--text-secondary); margin: 0 0 18px;
  }}
  .refresh-note strong {{ color: var(--text-primary); }}

  .stat-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 18px; }}
  .tile {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }}
  .tile .label {{ font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.03em; }}
  .tile .value {{ font-size: 1.35rem; font-weight: 600; margin-top: 2px; }}
  .tile .delta {{ font-size: 0.78rem; margin-top: 2px; color: var(--text-secondary); }}
  .tile .delta.critical {{ color: var(--critical); }}
  .tile .delta.warning {{ color: var(--warning); }}

  .card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-bottom: 18px; }}
  .card h2 {{ font-size: 1.05rem; margin: 0 0 4px; }}
  .desc {{ color: var(--text-secondary); font-size: 0.85rem; margin: 0 0 10px; }}

  .legend {{ display: flex; flex-wrap: wrap; gap: 10px 16px; margin-bottom: 10px; }}
  .legend .item {{ display: flex; align-items: center; gap: 6px; font-size: 0.8rem; cursor: pointer; user-select: none; color: var(--text-secondary); }}
  .legend .item.dim {{ opacity: 0.35; }}
  .swatch {{ width: 10px; height: 10px; border-radius: 2px; display: inline-block; }}

  .chart-wrap {{ position: relative; }}
  svg.chart {{ width: 100%; height: 320px; display: block; overflow: visible; }}
  .tooltip {{
    position: absolute; pointer-events: none; background: var(--surface-1); border: 1px solid var(--border);
    border-radius: 8px; padding: 8px 10px; font-size: 0.78rem; box-shadow: 0 2px 10px rgba(0,0,0,0.12);
    display: none; min-width: 140px; z-index: 5;
  }}
  .tt-week {{ font-weight: 600; margin-bottom: 4px; }}
  .tt-row {{ display: flex; justify-content: space-between; gap: 12px; }}
  .tt-row .sw {{ width: 8px; height: 8px; border-radius: 2px; display: inline-block; margin-right: 5px; }}
  .tt-row .val {{ font-variant-numeric: tabular-nums; }}

  table.dq-table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; }}
  table.dq-table th, table.dq-table td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--gridline); }}
  table.dq-table th {{ color: var(--text-muted); font-weight: 500; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.02em; }}
  table.dq-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .status-pill {{ display: inline-flex; align-items: center; gap: 5px; padding: 2px 8px; border-radius: 999px; font-size: 0.72rem; font-weight: 600; }}
  .status-pill .dot {{ width: 6px; height: 6px; border-radius: 50%; display: inline-block; }}
  .status-pill.good {{ background: rgba(12,163,12,0.12); color: var(--good); }}
  .status-pill.good .dot {{ background: var(--good); }}
  .status-pill.warning {{ background: rgba(250,178,25,0.15); color: #9a6a04; }}
  :root[data-theme="dark"] .status-pill.warning {{ color: var(--warning); }}
  .status-pill.warning .dot {{ background: var(--warning); }}
  .status-pill.critical {{ background: rgba(208,59,59,0.12); color: var(--critical); }}
  .status-pill.critical .dot {{ background: var(--critical); }}
  .status-pill.no_data {{ background: rgba(137,135,129,0.15); color: var(--text-muted); }}
  .status-pill.no_data .dot {{ background: var(--text-muted); }}

  .footer {{ font-size: 0.75rem; color: var(--text-muted); margin-top: 12px; }}
</style>
</head>
<body>
<div class="viz-root page">

  <div class="banner">
    <h1>{title}</h1>
    <p class="sub">{pair_count} check/table pair(s) &middot; {week_count} week(s) &middot; {week_range} &middot; {distribution_scope} distribution</p>
  </div>

  <div class="scope-note">
    <strong>Scope:</strong> {distribution_scope}-distribution, non-Confidential data.
    This report is uncertified (Draft status) &mdash; it has not gone through
    the Certification review in 06-bi-reporting/06-policies.md (BIPOL-1,
    BIPOL-2) and must not be distributed Organization-wide or Externally
    on this basis. No Row-Level Security is applied (BIPOL-3): every row
    of the source extract is visible in this file to anyone who opens it.
  </div>

  <p class="refresh-note"><strong>Refresh schedule (BIPOL-4):</strong> {refresh_schedule} &middot; generated {generated_at} from a static data extract &mdash; this file does not update itself.</p>

  <div class="stat-row" id="statRow"></div>

  <div class="card">
    <h2>Weekly Pass Rate</h2>
    <p class="desc">Weekly pass rate by check &amp; table. Click a legend item to isolate a series; hover the chart for exact values.</p>
    <div class="legend" id="legend"></div>
    <div class="chart-wrap">
      <svg class="chart" id="chart" viewBox="0 0 920 320" preserveAspectRatio="none"></svg>
      <div class="tooltip" id="tooltip"></div>
    </div>
  </div>

  <div class="card">
    <h2>Latest Week Status &mdash; {latest_week}</h2>
    <p class="desc">Sorted worst pass rate first. Warn threshold {warn_pct}%, critical threshold {critical_pct}%.</p>
    <table class="dq-table" id="latestTable"></table>
  </div>

  <p class="footer">Generated by skill-lib/build-bi-report-v1 from {source_note}. Internal-distribution, non-Confidential data only &mdash; do not point this report at Confidential/Restricted/PII sources without adding Row-Level Security separately (BIPOL-3).</p>

</div>

<script>
const DASHBOARD_DATA = {data_json};
const COLORS = ['--series-1','--series-2','--series-3','--series-4','--series-5','--series-6','--series-7','--series-8'];

function colorFor(i) {{ return COLORS[i % COLORS.length]; }}

function fmtPct(v) {{ return v === null || v === undefined ? '—' : (v * 100).toFixed(1) + '%'; }}

function tile(label, value, deltaText, deltaClass) {{
  const d = document.createElement('div');
  d.className = 'tile';
  d.innerHTML = '<div class="label"></div><div class="value"></div>' +
    (deltaText ? '<div class="delta ' + (deltaClass || '') + '"></div>' : '');
  d.querySelector('.label').textContent = label;
  d.querySelector('.value').textContent = value;
  if (deltaText) d.querySelector('.delta').textContent = deltaText;
  return d;
}}

function renderTiles() {{
  const t = DASHBOARD_DATA.tiles;
  const row = document.getElementById('statRow');
  row.appendChild(tile('Check/Table Pairs', t.pair_count));
  row.appendChild(tile('Weeks Covered', t.week_count));
  row.appendChild(tile('Latest Overall Pass Rate', fmtPct(t.overall_latest_rate)));
  const belowClass = t.critical_count > 0 ? 'critical' : (t.below_warn_count > 0 ? 'warning' : '');
  row.appendChild(tile('Pairs Below Warn Threshold', t.below_warn_count, t.critical_count + ' critical', belowClass));
  if (t.worst_pair_label) {{
    row.appendChild(tile('Worst Pair (Latest Week)', fmtPct(t.worst_pair_rate), t.worst_pair_label, 'critical'));
  }}
}}

let activeSeries = new Set(DASHBOARD_DATA.series.map((s, i) => i));

function renderLegend() {{
  const legend = document.getElementById('legend');
  legend.innerHTML = '';
  DASHBOARD_DATA.series.forEach((s, i) => {{
    const item = document.createElement('span');
    item.className = 'item' + (activeSeries.has(i) ? '' : ' dim');
    const sw = document.createElement('span');
    sw.className = 'swatch';
    sw.style.background = 'var(' + colorFor(i) + ')';
    const name = document.createElement('span');
    name.className = 'name';
    name.textContent = s.label;
    item.appendChild(sw);
    item.appendChild(name);
    item.addEventListener('click', () => {{
      if (activeSeries.has(i)) {{ activeSeries.delete(i); }} else {{ activeSeries.add(i); }}
      renderLegend();
      drawChart();
    }});
    legend.appendChild(item);
  }});
}}

const svg = document.getElementById('chart');
const tooltip = document.getElementById('tooltip');
const padL = 42, padR = 12, padT = 12, padB = 26;
const plotW = 920 - padL - padR;
const plotH = 320 - padT - padB;
const weeks = DASHBOARD_DATA.weeks;

function xFor(i) {{ return padL + (weeks.length > 1 ? (i / (weeks.length - 1)) * plotW : plotW / 2); }}
function yFor(v) {{ return padT + (1 - v) * plotH; }}

function drawChart() {{
  svg.innerHTML = '';
  const ns = 'http://www.w3.org/2000/svg';

  for (let g = 0; g <= 4; g++) {{
    const v = g / 4;
    const y = yFor(v);
    const line = document.createElementNS(ns, 'line');
    line.setAttribute('x1', padL); line.setAttribute('x2', 920 - padR);
    line.setAttribute('y1', y); line.setAttribute('y2', y);
    line.setAttribute('stroke', 'var(--gridline)'); line.setAttribute('stroke-width', '1');
    svg.appendChild(line);
    const label = document.createElementNS(ns, 'text');
    label.setAttribute('x', padL - 6); label.setAttribute('y', y + 4);
    label.setAttribute('text-anchor', 'end'); label.setAttribute('font-size', '10');
    label.setAttribute('fill', 'var(--text-muted)');
    label.textContent = Math.round(v * 100) + '%';
    svg.appendChild(label);
  }}

  const tickEvery = Math.max(1, Math.ceil(weeks.length / 8));
  weeks.forEach((w, i) => {{
    if (i % tickEvery !== 0 && i !== weeks.length - 1) return;
    const x = xFor(i);
    const label = document.createElementNS(ns, 'text');
    label.setAttribute('x', x); label.setAttribute('y', 320 - 6);
    label.setAttribute('text-anchor', 'middle'); label.setAttribute('font-size', '10');
    label.setAttribute('fill', 'var(--text-muted)');
    label.textContent = w.slice(5);
    svg.appendChild(label);
  }});

  DASHBOARD_DATA.series.forEach((s, i) => {{
    if (!activeSeries.has(i)) return;
    const byWeek = {{}};
    s.points.forEach(p => {{ byWeek[p.week] = p.pass_rate; }});
    const pts = [];
    weeks.forEach((w, wi) => {{
      if (byWeek[w] === undefined) return;
      pts.push([xFor(wi), yFor(byWeek[w])]);
    }});
    if (pts.length === 0) return;
    const poly = document.createElementNS(ns, 'polyline');
    poly.setAttribute('points', pts.map(p => p[0] + ',' + p[1]).join(' '));
    poly.setAttribute('fill', 'none');
    poly.setAttribute('stroke', 'var(' + colorFor(i) + ')');
    poly.setAttribute('stroke-width', '2');
    svg.appendChild(poly);
    pts.forEach(p => {{
      const dot = document.createElementNS(ns, 'circle');
      dot.setAttribute('cx', p[0]); dot.setAttribute('cy', p[1]); dot.setAttribute('r', '2.5');
      dot.setAttribute('fill', 'var(' + colorFor(i) + ')');
      svg.appendChild(dot);
    }});
  }});

  const hoverLine = document.createElementNS(ns, 'line');
  hoverLine.setAttribute('y1', padT); hoverLine.setAttribute('y2', 320 - padB);
  hoverLine.setAttribute('stroke', 'var(--baseline)'); hoverLine.setAttribute('stroke-width', '1');
  hoverLine.setAttribute('visibility', 'hidden');
  svg.appendChild(hoverLine);

  const rect = document.createElementNS(ns, 'rect');
  rect.setAttribute('x', padL); rect.setAttribute('y', padT);
  rect.setAttribute('width', plotW); rect.setAttribute('height', plotH);
  rect.setAttribute('fill', 'transparent');
  svg.appendChild(rect);

  rect.addEventListener('mousemove', (evt) => {{
    const box = svg.getBoundingClientRect();
    const relX = (evt.clientX - box.left) / box.width * 920;
    let idx = 0;
    let best = Infinity;
    weeks.forEach((w, i) => {{
      const d = Math.abs(xFor(i) - relX);
      if (d < best) {{ best = d; idx = i; }}
    }});
    const week = weeks[idx];
    hoverLine.setAttribute('x1', xFor(idx)); hoverLine.setAttribute('x2', xFor(idx));
    hoverLine.setAttribute('visibility', 'visible');

    let htmlStr = '<div class="tt-week"></div>';
    tooltip.innerHTML = htmlStr;
    tooltip.querySelector('.tt-week').textContent = week;
    DASHBOARD_DATA.series.forEach((s, i) => {{
      if (!activeSeries.has(i)) return;
      const p = s.points.find(pt => pt.week === week);
      if (!p) return;
      const row = document.createElement('div');
      row.className = 'tt-row';
      const left = document.createElement('span');
      const sw = document.createElement('span');
      sw.className = 'sw';
      sw.style.background = 'var(' + colorFor(i) + ')';
      left.appendChild(sw);
      left.appendChild(document.createTextNode(s.label));
      const right = document.createElement('span');
      right.className = 'val';
      right.textContent = fmtPct(p.pass_rate);
      row.appendChild(left);
      row.appendChild(right);
      tooltip.appendChild(row);
    }});
    tooltip.style.display = 'block';
    tooltip.style.left = Math.min(box.width - 160, Math.max(0, (relX / 920) * box.width)) + 'px';
    tooltip.style.top = '4px';
  }});
  rect.addEventListener('mouseleave', () => {{
    tooltip.style.display = 'none';
    hoverLine.setAttribute('visibility', 'hidden');
  }});
}}

function renderLatestTable() {{
  const t = document.getElementById('latestTable');
  const labels = {{ good: 'On Target', warning: 'Warning', critical: 'Critical', no_data: 'No Data' }};
  let html = '<thead><tr><th>Check</th><th>Table</th><th class="num">Pass</th><th class="num">Fail</th><th class="num">Pass Rate</th><th>Status</th></tr></thead><tbody>';
  DASHBOARD_DATA.latest_table.forEach(r => {{
    html += '<tr>' +
      '<td>' + escapeHtml(r.check_name) + '</td>' +
      '<td>' + escapeHtml(r.table_name) + '</td>' +
      '<td class="num">' + (r.pass_count === null ? '—' : r.pass_count.toLocaleString()) + '</td>' +
      '<td class="num">' + (r.fail_count === null ? '—' : r.fail_count.toLocaleString()) + '</td>' +
      '<td class="num">' + fmtPct(r.pass_rate) + '</td>' +
      '<td><span class="status-pill ' + r.status + '"><span class="dot"></span>' + labels[r.status] + '</span></td>' +
      '</tr>';
  }});
  html += '</tbody>';
  t.innerHTML = html;
}}

function escapeHtml(s) {{
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}}

renderTiles();
renderLegend();
drawChart();
renderLatestTable();
</script>
</body>
</html>
"""


def render_html(dashboard_data, title, refresh_schedule, distribution_scope, source_note, generated_at):
    tiles = dashboard_data["tiles"]
    return HTML_TEMPLATE.format(
        title=escape(title),
        pair_count=tiles["pair_count"],
        week_count=tiles["week_count"],
        week_range=escape(tiles["week_range"]),
        distribution_scope=escape(distribution_scope),
        refresh_schedule=escape(refresh_schedule),
        generated_at=escape(generated_at),
        latest_week=escape(tiles["latest_week"]),
        warn_pct=round(dashboard_data["warn_threshold"] * 100, 1),
        critical_pct=round(dashboard_data["critical_threshold"] * 100, 1),
        source_note=escape(source_note),
        data_json=json.dumps(dashboard_data),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a self-contained HTML BI dashboard from a weekly data-quality-metrics CSV "
        "(skill-lib/build-bi-report-v1). Internal-distribution, non-Confidential data only."
    )
    parser.add_argument("input", help="Path to the source CSV (check_name, table_name, week_ending, "
                                       "pass_count, fail_count, pass_rate).")
    parser.add_argument("output", help="Path to write the generated HTML dashboard to.")
    parser.add_argument(
        "--refresh-schedule",
        required=True,
        help="Declared Report Refresh Schedule text (BIPOL-4), e.g. "
        "'Weekly, Mondays 06:00 UTC'. Required - this script will not guess "
        "or default a refresh cadence for you.",
    )
    parser.add_argument(
        "--title",
        default="Weekly Data Quality Dashboard",
        help="Dashboard page title (default: 'Weekly Data Quality Dashboard').",
    )
    parser.add_argument(
        "--distribution-scope",
        default="Internal",
        choices=["Internal", "Departmental"],
        help="Distribution Scope label rendered in the output (default: Internal). "
        "This Skill does not support Organization-wide or External scope - those "
        "require Certified status (BIPOL-1), which this Skill does not implement.",
    )
    parser.add_argument(
        "--warn-threshold",
        type=float,
        default=0.95,
        help="Pass rate at/above which a pair's latest-week status is 'On Target' (default: 0.95).",
    )
    parser.add_argument(
        "--critical-threshold",
        type=float,
        default=0.80,
        help="Pass rate at/above which (but below --warn-threshold) a pair's latest-week status is "
        "'Warning' rather than 'Critical' (default: 0.80).",
    )
    parser.add_argument(
        "--source-note",
        default=None,
        help="Short description of the source extract for the footer (default: the input filename).",
    )
    args = parser.parse_args()

    if not (0.0 <= args.critical_threshold <= args.warn_threshold <= 1.0):
        print("Error: require 0 <= --critical-threshold <= --warn-threshold <= 1", file=sys.stderr)
        return 2
    if not args.refresh_schedule.strip():
        print("Error: --refresh-schedule must not be empty (BIPOL-4 requires a declared schedule)", file=sys.stderr)
        return 2

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 2

    try:
        rows = read_rows(input_path)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    dashboard_data = build_dashboard_data(rows, args.warn_threshold, args.critical_threshold)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    source_note = args.source_note or input_path.name

    html_out = render_html(
        dashboard_data,
        title=args.title,
        refresh_schedule=args.refresh_schedule,
        distribution_scope=args.distribution_scope,
        source_note=source_note,
        generated_at=generated_at,
    )

    output_path = Path(args.output)
    output_path.write_text(html_out, encoding="utf-8")

    tiles = dashboard_data["tiles"]
    print(
        f"Wrote {output_path} ({tiles['pair_count']} pairs x {tiles['week_count']} weeks, "
        f"latest week {tiles['latest_week']}, {tiles['below_warn_count']} pair(s) below warn threshold)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
