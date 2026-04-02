#!/usr/bin/env python3
"""
ShootMesh-AI entrypoint: multi-agent merge for a synthetic production day.

Experimental PoC only — not on-set or production guidance.
"""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from shootmesh.engine import run_production_day  # noqa: E402
from shootmesh.plots import plot_agent_influence, plot_slippage_timeline  # noqa: E402
from shootmesh.reporting import ascii_table, ledger_to_rows  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="ShootMesh-AI experimental coordinator demo")
    parser.add_argument("--seed", type=int, default=42, help="reserved for future stochastic runs")
    args = parser.parse_args()

    out_dir = os.path.join(ROOT, "output")
    os.makedirs(out_dir, exist_ok=True)

    summary = run_production_day(seed=args.seed)
    rows = ledger_to_rows(summary.ledger)
    table = ascii_table(["step", "department", "shift_min", "incident (truncated)"], rows)

    print("=" * 78)
    print("  ShootMesh-AI — experimental production-day coordination PoC")
    print("=" * 78)
    print()
    print(table)
    print()
    print(
        f"Incidents simulated: {summary.total_incidents} | "
        f"Total slippage (minutes): {summary.total_slippage_min}"
    )
    print()

    plot_agent_influence(
        summary.agent_weights,
        os.path.join(out_dir, "agent_influence.png"),
    )
    plot_slippage_timeline(
        [e.resulting_shift_min for e in summary.ledger],
        os.path.join(out_dir, "slippage_timeline.png"),
    )
    print(f"Wrote charts under: {out_dir}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
