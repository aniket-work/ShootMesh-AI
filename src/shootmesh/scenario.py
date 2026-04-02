"""Synthetic shooting-day incidents for the PoC."""

from __future__ import annotations

from shootmesh.types import Incident, IncidentKind


def default_day_incidents() -> list[Incident]:
    """A compact but realistic sequence of staged problems (experimental data)."""
    return [
        Incident(
            IncidentKind.WEATHER,
            "Sudden rain on the exterior lot; grip needs 25 minutes to re-rig",
            severity=3,
        ),
        Incident(
            IncidentKind.TALENT,
            "Supporting actor caught in traffic; earliest arrival +40 minutes",
            severity=4,
        ),
        Incident(
            IncidentKind.GEAR,
            "Camera body intermittent error; swap body +15 minutes",
            severity=2,
        ),
        Incident(
            IncidentKind.LOCATION,
            "Adjacent unit is loud; need quiet window or move mic plan",
            severity=2,
        ),
        Incident(
            IncidentKind.PERMIT,
            "Noise curfew moved 30 minutes earlier by building management",
            severity=5,
        ),
    ]
