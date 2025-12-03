"""
RP-1 Engine Code Package

This package implements scaffolding for:
- Harm interpretation pipeline
- Intervention flow and authority decay
- Decision and dissolution logic
- Interfaces and storage for append-only ledgers

All logic here should conform to the RP-1 documentation in the ENGINE folder.
Nothing here should create long-term control; it should only support detection,
classification, temporary intervention, logging, and dissolution.
"""

from .models import (
    HarmSignal,
    HarmTier,
    Domain,
    Decision,
    InterventionWindow,
    TribunalRuling,
)
from .harm_pipeline import HarmInterpreter
from .intervention_flow import InterventionCoordinator
from .decision_engine import DecisionEngine