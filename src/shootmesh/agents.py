"""Department-style agents that emit ranked proposals."""

from __future__ import annotations

from shootmesh.types import Incident, IncidentKind, Priority, Proposal


class DepartmentAgent:
    role: str

    def propose(self, incident: Incident) -> list[Proposal]:
        raise NotImplementedError


class SchedulingAgent(DepartmentAgent):
    role = "scheduling"

    def propose(self, incident: Incident) -> list[Proposal]:
        if incident.kind == IncidentKind.TALENT:
            return [
                Proposal(
                    self.role,
                    "Slide block 2 after lunch; protect golden hour exterior",
                    Priority.SCHEDULE,
                    minutes_shift=25,
                    confidence=0.82,
                ),
                Proposal(
                    self.role,
                    "Swap two dialogue scenes to free later unit time",
                    Priority.SCHEDULE,
                    minutes_shift=20,
                    confidence=0.74,
                ),
            ]
        if incident.kind == IncidentKind.PERMIT:
            return [
                Proposal(
                    self.role,
                    "Compress turnaround; stagger department breaks",
                    Priority.SCHEDULE,
                    minutes_shift=35,
                    confidence=0.71,
                )
            ]
        return [
            Proposal(
                self.role,
                "Re-sequence setups to absorb slip without dropping pages",
                Priority.SCHEDULE,
                minutes_shift=15,
                confidence=0.68,
            )
        ]


class LocationsAgent(DepartmentAgent):
    role = "locations"

    def propose(self, incident: Incident) -> list[Proposal]:
        if incident.kind == IncidentKind.WEATHER:
            return [
                Proposal(
                    self.role,
                    "Pivot to covered porch set; pre-lit interior backup",
                    Priority.SCHEDULE,
                    minutes_shift=25,
                    confidence=0.77,
                ),
                Proposal(
                    self.role,
                    "Hold for cell pass; shoot pickups on stage tomorrow",
                    Priority.COST,
                    minutes_shift=120,
                    confidence=0.55,
                ),
            ]
        if incident.kind == IncidentKind.LOCATION:
            return [
                Proposal(
                    self.role,
                    "Negotiate 20-minute quiet window with neighbor unit",
                    Priority.SCHEDULE,
                    minutes_shift=20,
                    confidence=0.7,
                ),
                Proposal(
                    self.role,
                    "Relocate one angle to stairwell (pre-scouted)",
                    Priority.CREATIVE,
                    minutes_shift=35,
                    confidence=0.62,
                ),
            ]
        return [
            Proposal(
                self.role,
                "Confirm holding area; adjust base camp footprint",
                Priority.SCHEDULE,
                minutes_shift=10,
                confidence=0.6,
            )
        ]


class SafetyAgent(DepartmentAgent):
    role = "safety"

    def propose(self, incident: Incident) -> list[Proposal]:
        if incident.kind == IncidentKind.WEATHER:
            return [
                Proposal(
                    self.role,
                    "Delay exterior until rain cell passes; no wet lifts",
                    Priority.SAFETY,
                    minutes_shift=35,
                    confidence=0.9,
                )
            ]
        if incident.kind == IncidentKind.GEAR:
            return [
                Proposal(
                    self.role,
                    "Full stop until body swap verified; test record loop",
                    Priority.SAFETY,
                    minutes_shift=15,
                    confidence=0.93,
                )
            ]
        if incident.kind == IncidentKind.PERMIT:
            return [
                Proposal(
                    self.role,
                    "Hard stop at curfew; no exceptions without exec sign-off",
                    Priority.SAFETY,
                    minutes_shift=30,
                    confidence=0.86,
                )
            ]
        return []


class EquipmentAgent(DepartmentAgent):
    role = "equipment"

    def propose(self, incident: Incident) -> list[Proposal]:
        if incident.kind == IncidentKind.GEAR:
            return [
                Proposal(
                    self.role,
                    "Swap A-camera body from truck kit; minimal lens change",
                    Priority.SCHEDULE,
                    minutes_shift=15,
                    confidence=0.88,
                ),
                Proposal(
                    self.role,
                    "Use B-camera as A for scene 12 only; rebalance tomorrow",
                    Priority.COST,
                    minutes_shift=8,
                    confidence=0.66,
                ),
            ]
        return [
            Proposal(
                self.role,
                "Pre-stage backup distro; avoid cable runs across traffic",
                Priority.SCHEDULE,
                minutes_shift=10,
                confidence=0.7,
            )
        ]


def all_department_agents() -> list[DepartmentAgent]:
    return [
        SchedulingAgent(),
        LocationsAgent(),
        SafetyAgent(),
        EquipmentAgent(),
    ]
