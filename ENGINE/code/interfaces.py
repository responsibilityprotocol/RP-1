from __future__ import annotations

from typing import Protocol, Iterable

from .models import HarmSignal, ValidatedHarm, Decision, TribunalRuling


class HarmSignalSource(Protocol):
    """Abstract source of harm signals (logs, reports, sensors, etc.)."""

    def stream_signals(self) -> Iterable[HarmSignal]:
        ...


class TribunalNotifier(Protocol):
    """Interface for notifying or integrating with a Tribunal system."""

    def notify_decision(self, decision: Decision) -> None:
        ...

    def submit_ruling(self, ruling: TribunalRuling) -> None:
        ...


class CreatorNotifier(Protocol):
    """Interface for notifying system creators about redesign duties."""

    def notify_redesign_required(self, validated_harm: ValidatedHarm) -> None:
        ...