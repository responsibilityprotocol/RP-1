from __future__ import annotations

from datetime import datetime, timedelta

from .models import InterventionWindow, ValidatedHarm


DEFAULT_INTERVENTION_HOURS = 12
MAX_INTERVENTION_HOURS = 72


def create_intervention_window(
    harm: ValidatedHarm,
    now: datetime | None = None,
) -> InterventionWindow:
    """
    Create a new intervention window with:
    - default 12 hour expiry
    - hard 72 hour maximum lifetime
    """
    now = now or datetime.utcnow()
    default_expiry = now + timedelta(hours=DEFAULT_INTERVENTION_HOURS)
    max_expiry = now + timedelta(hours=MAX_INTERVENTION_HOURS)
    return InterventionWindow(
        id=f"iw_{harm.signal.id}_{int(now.timestamp())}",
        harm=harm,
        opened_at=now,
        expires_at=default_expiry,
        max_expires_at=max_expiry,
    )


def renew_intervention_window(
    window: InterventionWindow,
    now: datetime | None = None,
) -> InterventionWindow:
    """
    Attempt to renew an intervention window.

    This function should only be called when fresh multi-domain concurrence
    confirms harm is still active at T3–T5. This scaffold does not enforce
    that validation; callers are responsible for checking before renewal.
    """
    now = now or datetime.utcnow()
    if window.is_expired(now):
        # No further renewal allowed; caller should log a failure.
        window.active = False
        return window

    new_expiry = now + timedelta(hours=DEFAULT_INTERVENTION_HOURS)
    if new_expiry > window.max_expires_at:
        # Cannot exceed hard cap
        window.expires_at = window.max_expires_at
        window.active = False
    else:
        window.expires_at = new_expiry
        window.renewed_count += 1

    return window