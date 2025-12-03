"""
Example RP-1 Engine Pipeline

This file shows how the scaffolded components in the ENGINE/code package
can be wired together:

1. Receive a harm signal
2. Run it through the Harm Interpreter
3. Possibly open an intervention window
4. Generate a decision with dissolution conditions
5. Append everything to an append-only ledger

This is ONLY a demonstration harness, not a production implementation.
"""

from datetime import datetime
from pathlib import Path

from models import (
    HarmSignal,
    Domain,
)
from harm_pipeline import HarmInterpreter
from intervention_flow import InterventionCoordinator
from decision_engine import DecisionEngine
from storage import FileAppendOnlyLedger


def main() -> None:
    # 1. Set up a simple file-backed append-only ledger
    ledger_root = Path("./engine_ledger")
    ledger = FileAppendOnlyLedger(ledger_root)

    # 2. Create the engine components
    interpreter = HarmInterpreter()
    coordinator = InterventionCoordinator(ledger=ledger)
    decision_engine = DecisionEngine(ledger=ledger)

    # 3. Example harm signal (you can change this to test different paths)
    signal = HarmSignal(
        id="sig_001",
        domains=[Domain.HUMAN, Domain.ECOLOGICAL],
        description=(
            "Reported strain on local aquifer and dust storms increasing "
            "after new AI datacenter construction, with community health impacts."
        ),
        evidence_refs=["report://community_health_2025", "env://aquifer_metrics_q1"],
        reported_at=datetime.utcnow(),
        involves_minors=False,
        involves_species_risk=True,  # triggers T3+ heuristics
    )

    # 4. Interpret and validate harm
    validated = interpreter.validate(signal)
    print(f"[INTERPRET] Tier: {validated.tier}, Notes: {validated.validation_notes}")

    # 5. Possibly open an intervention window (T3+)
    window = coordinator.maybe_open_window(validated)
    if window is None:
        print("[INTERVENTION] No intervention window opened (T1/T2).")
    else:
        print(
            f"[INTERVENTION] Window opened: {window.id}, "
            f"expires_at={window.expires_at.isoformat()}, "
            f"max_expires_at={window.max_expires_at.isoformat()}"
        )

    # 6. Generate a decision with dissolution conditions
    decision = decision_engine.make_decision(validated, window=window)
    print("[DECISION]")
    print(f"  id: {decision.id}")
    print(f"  recommended_actions:")
    for a in decision.recommended_actions:
        print(f"    - {a}")
    print(f"  dissolution_condition: {decision.dissolution_condition}")

    print("\nAll events appended to the append-only ledger at:", ledger_root.resolve())


if __name__ == "__main__":
    main()