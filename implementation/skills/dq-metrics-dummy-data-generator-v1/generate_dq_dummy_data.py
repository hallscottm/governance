#!/usr/bin/env python3
"""
generate_dq_dummy_data.py

Generates a synthetic "weekly data-quality metrics" CSV, shaped like a
real BI/data-quality export: one row per (check_name, table_name,
week_ending), columns:

    check_name, table_name, week_ending, pass_count, fail_count, pass_rate

Parameters (all via CLI flags): number of weeks to simulate, number of
distinct (check, table) pairs, and a random seed. The same seed always
produces the same output (byte-for-byte), which matters for eval
reproducibility - all randomness is drawn from a single seeded
random.Random instance, and no other source of non-determinism
(wall-clock time, dict/set iteration order across pairs, etc.) affects
the generated rows.

Modeling notes (why the numbers look the way they do, not just
random(0, 100) per row):

  - Each (check, table) pair gets a fixed "baseline quality" drawn from
    a Beta distribution skewed high (alpha=14, beta=1.3, mean ~0.915),
    matching how real data-quality checks behave: most checks on most
    tables pass the large majority of the time, a minority of pairs
    are somewhat flakier than the rest, and essentially none sit at a
    50/50 coin-flip.
  - Within a pair, week-to-week pass rate wobbles slightly around that
    baseline (small Gaussian noise) rather than being identical every
    week, to mimic ordinary operational variance.
  - Each pair also gets a small independent chance per week of a "bad
    week" (an incident, a late upstream load, a schema drift) where
    pass rate drops sharply for that week only - occasional, not
    constant, and the baseline recovers the following week.
  - Row volume (pass_count + fail_count) varies per pair/week within a
    plausible range for a daily-batch check rolled up weekly, rather
    than being a fixed constant.

Standard-library only (argparse, csv, datetime, random). No network
access, no third-party dependencies, no writes outside the given
output path.

Usage:
    python3 generate_dq_dummy_data.py <output.csv> --weeks 8 --pairs 5 --seed 42
"""

import argparse
import csv
import sys
from datetime import date, timedelta
from pathlib import Path
import random

CHECK_NAMES = [
    "not_null",
    "unique_key",
    "referential_integrity",
    "row_count_within_bounds",
    "freshness_sla",
    "schema_match",
    "value_range",
    "duplicate_rows",
    "format_pattern",
    "accepted_values",
]

TABLE_NAMES = [
    "orders",
    "customers",
    "payments",
    "shipments",
    "inventory_snapshots",
    "product_catalog",
    "support_tickets",
    "marketing_events",
    "user_sessions",
    "returns",
]


def build_pairs(num_pairs: int, rng: random.Random) -> list[tuple[str, str]]:
    """Deterministically build num_pairs distinct (check_name, table_name)
    pairs from the fixed name lists, using the seeded rng so the choice
    of pairs is itself reproducible for a given seed."""
    all_combos = [(c, t) for c in CHECK_NAMES for t in TABLE_NAMES]
    rng.shuffle(all_combos)

    if num_pairs > len(all_combos):
        # Not enough distinct (check, table) combos left in the fixed
        # name lists - extend with numbered suffixes rather than
        # silently truncating the requested pair count.
        pairs = list(all_combos)
        i = 0
        while len(pairs) < num_pairs:
            c = CHECK_NAMES[i % len(CHECK_NAMES)]
            t = f"{TABLE_NAMES[i % len(TABLE_NAMES)]}_{i // len(TABLE_NAMES) + 2}"
            pairs.append((c, t))
            i += 1
        return pairs[:num_pairs]

    return all_combos[:num_pairs]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a synthetic weekly data-quality metrics CSV."
    )
    parser.add_argument("output", help="Path to write the output CSV to.")
    parser.add_argument(
        "--weeks", type=int, default=8, help="Number of weeks to simulate (default: 8)."
    )
    parser.add_argument(
        "--pairs",
        type=int,
        default=5,
        help="Number of distinct (check, table) pairs to simulate (default: 5).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed. Same seed + same --weeks/--pairs always produces "
        "identical output (default: 0).",
    )
    parser.add_argument(
        "--anchor-date",
        type=str,
        default="2026-09-21",
        help="ISO date (YYYY-MM-DD) used as the most recent week_ending "
        "(default: 2026-09-21, a fixed Monday so output doesn't drift "
        "with wall-clock time run-to-run).",
    )
    args = parser.parse_args()

    if args.weeks < 1:
        print("Error: --weeks must be >= 1", file=sys.stderr)
        return 2
    if args.pairs < 1:
        print("Error: --pairs must be >= 1", file=sys.stderr)
        return 2

    try:
        anchor = date.fromisoformat(args.anchor_date)
    except ValueError:
        print(f"Error: --anchor-date must be ISO YYYY-MM-DD, got {args.anchor_date!r}", file=sys.stderr)
        return 2

    rng = random.Random(args.seed)

    pairs = build_pairs(args.pairs, rng)

    # Oldest week first, most recent (anchor) week last - reads like a
    # real time series export.
    weeks = [anchor - timedelta(weeks=offset) for offset in range(args.weeks - 1, -1, -1)]

    rows = []
    for check_name, table_name in pairs:
        # Fixed per-pair baseline quality, skewed high: most (check,
        # table) pairs pass the vast majority of the time; a handful
        # run somewhat flakier. alpha=14, beta=1.3 (mean ~0.915) keeps
        # the bulk of pairs comfortably in the high-90s while still
        # allowing a realistic lower tail, rather than a hard floor.
        baseline = rng.betavariate(14, 1.3)

        # Fixed per-pair typical weekly volume (rows checked per week),
        # varying by check/table rather than being constant across the
        # whole dataset.
        base_volume = rng.randint(300, 5000)

        for week_ending in weeks:
            # Small week-to-week operational noise around the baseline.
            noise = rng.gauss(0, 0.02)
            pass_rate = baseline + noise

            # Occasional bad week: ~6% chance per pair-week of an
            # incident that knocks pass_rate down sharply just for that
            # week (e.g. upstream schema drift, late-arriving batch).
            if rng.random() < 0.06:
                pass_rate -= rng.uniform(0.25, 0.70)

            pass_rate = max(0.0, min(1.0, pass_rate))

            # Weekly volume also wobbles a bit rather than being fixed.
            total = max(1, int(rng.gauss(base_volume, base_volume * 0.1)))

            pass_count = round(total * pass_rate)
            pass_count = max(0, min(total, pass_count))
            fail_count = total - pass_count

            # Recompute pass_rate from the actual integer counts so the
            # CSV's own numbers are internally consistent (pass_count +
            # fail_count == total, pass_rate == pass_count / total)
            # rather than carrying the pre-rounding float.
            actual_pass_rate = round(pass_count / total, 4) if total > 0 else 0.0

            rows.append(
                {
                    "check_name": check_name,
                    "table_name": table_name,
                    "week_ending": week_ending.isoformat(),
                    "pass_count": pass_count,
                    "fail_count": fail_count,
                    "pass_rate": actual_pass_rate,
                }
            )

    output_path = Path(args.output)
    fieldnames = ["check_name", "table_name", "week_ending", "pass_count", "fail_count", "pass_rate"]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(
        f"Wrote {output_path} ({len(rows)} rows: {len(pairs)} pairs x {args.weeks} weeks, seed={args.seed})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
