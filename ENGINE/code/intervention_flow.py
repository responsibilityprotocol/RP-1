from __future__ import annotations

from datetime import datetime

from .models import ValidatedHarm, InterventionWindow, HarmTier
from .storage import (
    AppendOnlyLedger,
    LEDGER_INTERVENTIONS,
    LEDGER_RENEWAL_FAILURES,
)
from .clocks import create_intervention_window, renew_intervention_window


class InterventionCoordinator:
    """
    Coordinates intervention windows according to INTERVENTION_FLOW.md:
    - Only T3–T5 harms may trigger interventions.
    - Windows are 12 hours by default, 72 hours max.
    - Authority must dissolve when harm ceases or time caps are reached.
    """

    def __init__(self, ledger: AppendOnlyLedger) -> None:
        self.ledger = ledger

    def maybe_open_window(
        self,
        harm: ValidatedHarm,
        now: datetime | None = None,
    ) -> InterventionWindow | None:
        if harm.tier in {HarmTier.T1_MINIMAL, HarmTier.T2_CONCERNING}:
            return None

        window = create_intervention_window(harm, now)
        self.ledger.append(LEDGER_INTERVENTIONS, window)
        return window

    def maybe_renew_window(
        self,
        window: InterventionWindow,
        harm_still_active: bool,
        now: datetime | None = None,
    ) -> InterventionWindow:
        """
        Caller is responsible for ensuring fresh multi-domain concurrence
        before setting harm_still_active=True.
        """
        if not harm_still_active:
            # mark inactive and log failure
            window.active = False
            self.ledger.append(LEDGER_RENEWAL_FAILURES, window)
            return window

        new_window = renew_intervention_window(window, now)
        if new_window.is_expired(now):
            self.ledger.append(LEDGER_RENEWAL_FAILURES, new_window)
        else:
            self.ledger.append(LEDGER_INTERVENTIONS, new_window)

        return new_window