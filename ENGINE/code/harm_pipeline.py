from __future__ import annotations

from datetime import datetime
from typing import List

from .models import HarmSignal, HarmTier, ValidatedHarm, Domain


class HarmInterpreter:
    """
    Implements the classification and validation rules described in
    HARM_INTERPRETATION_PIPELINE.md.

    This is a scaffold: real implementations should plug in analytics,
    monitoring, and contextual information.
    """

    def classify_tier(self, signal: HarmSignal) -> HarmTier:
        """
        Very simplified tier classification.

        You will eventually replace this with:
        - pattern analysis
        - ecological risk signals
        - minor/species risk heuristics
        - etc.
        """
        if signal.involves_minors or signal.involves_species_risk:
            return HarmTier.T3_HIGH

        # naive demo heuristics
        text = signal.description.lower()
        if "death" in text or "extinction" in text:
            return HarmTier.T5_EXTINCTION
        if "ecosystem" in text or "aquifer" in text or "collapse" in text:
            return HarmTier.T4_CASCADING
        if "injury" in text or "fraud" in text or "exploit" in text:
            return HarmTier.T3_HIGH
        if "disruption" in text or "instability" in text:
            return HarmTier.T2_CONCERNING
        return HarmTier.T1_MINIMAL

    def validate_domains(self, signal: HarmSignal) -> List[Domain]:
        """
        Placeholder multi-domain validation.
        For now, treats the domains on the signal as 'validated'.
        A real implementation would require independent verification.
        """
        return list(set(signal.domains))

    def validate(
        self,
        signal: HarmSignal,
        now: datetime | None = None,
    ) -> ValidatedHarm:
        """Produce a ValidatedHarm object from a raw signal."""
        now = now or datetime.utcnow()
        tier = self.classify_tier(signal)
        validated_domains = self.validate_domains(signal)

        notes = "Auto-classified based on description and flags."
        if signal.involves_minors:
            notes += " Minor/early cognition protection applied (>= T3)."
        if signal.involves_species_risk:
            notes += " Species/ecology risk applied (>= T3)."

        return ValidatedHarm(
            signal=signal,
            tier=tier,
            validated_domains=validated_domains,
            validation_notes=notes,
            validation_time=now,
        )