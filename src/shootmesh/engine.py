"""End-to-end simulation wiring agents, coordinator, and ledger."""

from __future__ import annotations

from shootmesh.agents import DepartmentAgent, all_department_agents
from shootmesh.coordinator import run_step
from shootmesh.scenario import default_day_incidents
from shootmesh.types import Incident, LedgerEntry, RunSummary


def collect_proposals(agents: list[DepartmentAgent], incident: Incident) -> list:
    proposals = []
    for agent in agents:
        proposals.extend(agent.propose(incident))
    return proposals


def run_production_day(seed: int | None = None) -> RunSummary:
    """Run the staged day. Seed is accepted for API symmetry; policy is deterministic."""
    _ = seed
    incidents = default_day_incidents()
    agents = all_department_agents()
    ledger: list[LedgerEntry] = []
    weights: dict[str, float] = {a.role: 0.0 for a in agents}
    slippage: list[int] = []

    for i, incident in enumerate(incidents, start=1):
        proposals = collect_proposals(agents, incident)
        entry = run_step(i, incident, proposals)
        ledger.append(entry)
        slippage.append(entry.resulting_shift_min)
        weights[entry.chosen_from] = weights.get(entry.chosen_from, 0.0) + 1.0

    total_w = sum(weights.values()) or 1.0
    agent_weights = {k: v / total_w for k, v in weights.items()}

    return RunSummary(
        total_incidents=len(incidents),
        total_slippage_min=sum(slippage),
        agent_weights=agent_weights,
        ledger=ledger,
    )
