from __future__ import annotations

from datetime import datetime
from typing import List

from .models import ValidatedHarm, Decision, HarmTier, InterventionWindow
from .storage import AppendOnlyLedger, LEDGER_DECISIONS


class DecisionEngine:
    """
    Generates decisions with dissolution conditions according to
    DECISION_AND_DISSOLUTION.md.

    This engine:
    - recommends restorative actions
    - encodes clear dissolution conditions
    - never grants open-ended authority
    """

    def __init__(self, ledger: AppendOnlyLedger) -> None:
        self.ledger = ledger

    def make_decision(
        self,
        harm: ValidatedHarm,
        window: InterventionWindow | None = None,
        now: datetime | None = None,
    ) -> Decision:
        now = now or datetime.utcnow()
        actions = self._recommend_actions(harm)
        dissolution = self._dissolution_condition_text(harm)

        decision = Decision(
            id=f"dec_{harm.signal.id}_{int(now.timestamp())}",
            harm=harm,
            recommended_actions=actions,
            created_at=now,
            dissolution_condition=dissolution,
        )
        self.ledger.append(LEDGER_DECISIONS, decision)
        return decision

    def _recommend_actions(self, harm: ValidatedHarm) -> List[str]:
        """
        Very high-level scaffolding. In reality, this would
        propose specific restorative steps, not punishment.
        """
        tier = harm.tier

        if tier == HarmTier.T1_MINIMAL:
            return ["Log incident; monitor for patterns; no intervention needed."]
        if tier == HarmTier.T2_CONCERNING:
            return ["Correlate similar signals; notify responsible maintainers; education focus."]
        if tier == HarmTier.T3_HIGH:
            return [
                "Convene Tribunal.",
                "Freeze relevant evidence under EII.",
                "Notify creators of redesign accountability requirement.",
            ]
        if tier == HarmTier.T4_CASCADING:
            return [
                "Convene Tribunal with ecological expertise.",
                "Map cascading impacts on species, water, and communities.",
                "Prioritize fastest restoration path; plan redesign.",
            ]
        if tier == HarmTier.T5_EXTINCTION:
            return [
                "Convene Tribunal immediately.",
                "Trigger emergency ecological and life-preservation review.",
                "Freeze harmful infrastructure actions where clearly harm-preventive.",
            ]
        return ["No recommendation (unexpected tier)."]

    def _dissolution_condition_text(self, harm: ValidatedHarm) -> str:
        """
        Encodes when authority must dissolve, per protocol:
        - when harm is resolved or stabilized
        - when autonomy and ecological cohesion are restored
        - when time caps are reached
        """
        return (
            "Authority dissolves when: (1) active harm ceases or is stabilized, "
            "(2) autonomy or ecological cohesion is restored, or "
            "(3) maximum intervention time window is reached."
        )