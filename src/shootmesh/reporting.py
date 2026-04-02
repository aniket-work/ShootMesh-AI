"""ASCII reporting for terminal-friendly demos."""

from __future__ import annotations

from shootmesh.types import LedgerEntry


def ascii_table(headers: list[str], rows: list[list[object]]) -> str:
    str_rows = [[str(c) for c in r] for r in rows]
    widths = [len(h) for h in headers]
    for r in str_rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(cell))
    sep = "+".join("-" * (w + 2) for w in widths)
    top = "+" + sep + "+"
    def fmt_row(cells: list[str]) -> str:
        parts = []
        for w, c in zip(widths, cells, strict=True):
            parts.append(f" {c:<{w}} ")
        return "|" + "|".join(parts) + "|"

    out = [top, fmt_row(headers), top]
    for r in str_rows:
        out.append(fmt_row(r))
    out.append(top)
    return "\n".join(out)


def ledger_to_rows(ledger: list[LedgerEntry]) -> list[list[object]]:
    rows: list[list[object]] = []
    for e in ledger:
        rows.append(
            [
                e.step,
                e.chosen_from,
                e.resulting_shift_min,
                (e.incident[:52] + "...")
                if len(e.incident) > 55
                else e.incident,
            ]
        )
    return rows
