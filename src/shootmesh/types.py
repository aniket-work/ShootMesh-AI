"""Shared types for production coordination."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal


class Priority(str, Enum):
    SAFETY = "safety"
    SCHEDULE = "schedule"
    CREATIVE = "creative"
    COST = "cost"


class IncidentKind(str, Enum):
    WEATHER = "weather"
    TALENT = "talent"
    GEAR = "gear"
    LOCATION = "location"
    PERMIT = "permit"


@dataclass(frozen=True)
class Proposal:
    agent: str
    summary: str
    priority: Priority
    minutes_shift: int
    confidence: float


@dataclass
class Incident:
    kind: IncidentKind
    description: str
    severity: int


@dataclass
class LedgerEntry:
    step: int
    incident: str
    chosen_from: str
    rationale: str
    resulting_shift_min: int


@dataclass
class RunSummary:
    total_incidents: int
    total_slippage_min: int
    agent_weights: dict[str, float]
    ledger: list[LedgerEntry] = field(default_factory=list)
