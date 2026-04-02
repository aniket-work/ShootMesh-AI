"""Coordinator merges proposals using a transparent priority policy."""

from __future__ import annotations

from shootmesh.types import Incident, LedgerEntry, Priority, Proposal


PRIORITY_ORDER: tuple[Priority, ...] = (
    Priority.SAFETY,
    Priority.SCHEDULE,
    Priority.CREATIVE,
    Priority.COST,
)


def choose_proposal(
    proposals: list[Proposal],
) -> tuple[Proposal, str]:
    """Deterministic selection: priority tier, then higher confidence, then lower slip."""
    if not proposals:
        raise ValueError("no proposals")

    def sort_key(p: Proposal) -> tuple[int, float, int]:
        tier = PRIORITY_ORDER.index(p.priority)
        return (-tier, p.confidence, -p.minutes_shift)

    ranked = sorted(proposals, key=sort_key, reverse=True)
    best = ranked[0]
    rationale = (
        f"selected {best.agent} ({best.priority.value}) "
        f"with confidence {best.confidence:.2f}; "
        f"alternatives considered: {len(ranked) - 1}"
    )
    return best, rationale


def run_step(
    step: int,
    incident: Incident,
    proposals: list[Proposal],
) -> LedgerEntry:
    best, rationale = choose_proposal(proposals)
    return LedgerEntry(
        step=step,
        incident=incident.description,
        chosen_from=best.agent,
        rationale=rationale,
        resulting_shift_min=best.minutes_shift,
    )
