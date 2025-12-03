from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Protocol, Iterable, Any
import json

from .models import (
    HarmSignal,
    ValidatedHarm,
    Decision,
    TribunalRuling,
    InterventionWindow,
)


class AppendOnlyLedger(Protocol):
    """Protocol describing an append-only ledger."""

    def append(self, record_type: str, record: Any) -> None:
        """Append a record to the ledger."""
        ...

    def iter_records(self, record_type: str) -> Iterable[dict]:
        """Iterate over records of a given type."""
        ...


class FileAppendOnlyLedger:
    """
    Very simple JSONL-based append-only ledger implementation.

    This is a scaffold: in a real system this might be a proper database or
    a cryptographically anchored log. The key property is: no deletion, no update.
    """

    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _file_for(self, record_type: str) -> Path:
        return self.root / f"{record_type}.jsonl"

    def append(self, record_type: str, record: Any) -> None:
        path = self._file_for(record_type)
        serialized = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": record_type,
            "payload": asdict(record),
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(serialized) + "\n")

    def iter_records(self, record_type: str):
        path = self._file_for(record_type)
        if not path.exists():
            return
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                yield json.loads(line)


# Convenience enum-like names for ledger types
LEDGER_HARM_SIGNALS = "harm_signals"
LEDGER_VALIDATED_HARM = "validated_harm"
LEDGER_DECISIONS = "decisions"
LEDGER_TRIBUNAL_RULINGS = "tribunal_rulings"
LEDGER_INTERVENTIONS = "interventions"
LEDGER_RENEWAL_FAILURES = "renewal_failures"