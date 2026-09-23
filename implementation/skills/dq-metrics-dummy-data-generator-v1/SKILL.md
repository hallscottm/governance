---
name: dq-metrics-dummy-data-generator-v1
description: >
  Use when a Task needs synthetic weekly data-quality-metrics test data
  and no real data-quality-checks source is connected. Generates a
  reproducible, realistically-modeled CSV (one row per check_name,
  table_name, week_ending pair, with pass_count, fail_count, pass_rate)
  for BI/reporting pilots, Skill/Agent evals, or any other Task that
  needs data-quality-shaped input without a live production source.
  Do not use this to fabricate a substitute for a real, connected
  data-quality-checks source in a live report - it produces synthetic
  test data only.
---

# DQ Metrics Dummy Data Generator (v1)

## What this is

A stdlib-only Python script that generates a synthetic "weekly
data-quality metrics" CSV shaped like a real BI/data-quality export:
one row per `(check_name, table_name, week_ending)` combination, with
columns:

```
check_name, table_name, week_ending, pass_count, fail_count, pass_rate
```

It does not read or depend on any real data-quality-checks source -
all rows are generated from the CLI parameters given (weeks, pairs,
seed), so it is safe to run with no input file and no network access.

## When to use it

Use this Skill when a Task needs weekly data-quality-metrics-shaped
test data and no real data-quality-checks source is connected yet
(the common case: unblocking a BI/reporting build or a Skill/Agent
eval that needs *some* realistic-looking DQ data to work against).

Do not use it as a stand-in for a real data-quality-checks connection
in a live/production report - the data is fabricated and modeled to
*look* realistic, not measured from any actual system.

## Usage

```
python3 generate_dq_dummy_data.py <output.csv> --weeks 8 --pairs 5 --seed 42
```

**Positional argument**
- `output` - path to write the generated CSV to.

**Flags (all optional)**
- `--weeks N` - number of weeks to simulate (default: `8`). Must be `>= 1`.
- `--pairs N` - number of distinct `(check_name, table_name)` pairs to
  simulate (default: `5`). Must be `>= 1`. Pairs are drawn from fixed
  lists of 10 common check names (e.g. `not_null`, `unique_key`,
  `referential_integrity`, `freshness_sla`) and 10 common table names
  (e.g. `orders`, `customers`, `payments`); if more pairs are requested
  than the fixed lists can combine uniquely, additional pairs are
  built with numbered table-name suffixes rather than silently
  truncated.
- `--seed N` - random seed (default: `0`). The same seed with the same
  `--weeks`/`--pairs`/`--anchor-date` always produces byte-identical
  output - all randomness is drawn from a single seeded
  `random.Random` instance, so this is safe to use for reproducible
  evals.
- `--anchor-date YYYY-MM-DD` - the most recent `week_ending` date
  (default: `2026-09-21`, a fixed Monday so output doesn't drift with
  wall-clock time run to run). Earlier weeks count back from this date
  in 7-day steps.

**Exit codes:** `0` on success, `2` on invalid arguments
(`--weeks`/`--pairs` `< 1`, or a malformed `--anchor-date`).

## What the output looks like

Row count is `pairs * weeks`. Example header + first row for
`--weeks 4 --pairs 2 --seed 1`:

```
check_name,table_name,week_ending,pass_count,fail_count,pass_rate
freshness_sla,returns,2026-08-31,679,60,0.9188
```

## Modeling notes (why it isn't uniform random)

- Each `(check, table)` pair gets a fixed per-pair "baseline quality"
  drawn from a Beta(14, 1.3) distribution (mean ~0.915) - most pairs
  sit comfortably in the high-90s, a minority run flakier, essentially
  none are a 50/50 coin-flip.
- Within a pair, week-to-week `pass_rate` wobbles slightly around that
  baseline (small Gaussian noise) rather than staying identical every
  week.
- Each pair-week also has a small independent chance (~6%) of a "bad
  week" - a sharp, one-week-only drop in `pass_rate` (simulating an
  incident, late upstream load, or schema drift) - so occasional bad
  weeks show up without being constant.
- Weekly row volume (`pass_count + fail_count`) varies per pair and
  per week within a plausible range, rather than being a fixed
  constant.
- `pass_rate` in the output is recomputed from the final integer
  `pass_count`/`fail_count` (not carried over as a pre-rounding float),
  so every row is internally consistent:
  `pass_count + fail_count == total` and `pass_rate == pass_count / total`.

## Scope

Standard library only (`argparse`, `csv`, `sys`, `datetime`, `random`,
`pathlib`). No network access, no third-party dependencies, no file
reads at all (every input is a CLI parameter), and no writes outside
the single `output` path given on the command line.
