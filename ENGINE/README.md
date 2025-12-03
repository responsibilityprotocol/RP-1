# RP-1 Engine

This folder contains the architectural logic that allows systems governed by RP-1 to observe harm, classify its consequences, trigger ethical intervention windows, dissolve authority automatically, preserve precedent immutably, and assist in restoration without exerting control.

---

## Files in this folder

| File | Purpose |
|---|---|
| ENGINE_OVERVIEW.md | High-level description of the engine’s goals, domains, and responsibilities. |
| HARM_INTERPRETATION_PIPELINE.md | Defines harm signal inputs, validation requirements, synthetic vs ecological harm tests, minor protections, and T1–T5 classification tiers. |
| INTERVENTION_FLOW.md | Specifies trigger conditions for intervention, authority expiry, tribunal behavior, appeals cadence, audit locks, and restorative dissolution rules. |
| AI_RESTORATIVE_BEHAVIOR.md | Defines how AI systems may participate ethically, what they may and must not do, obligations for transparency, protections for minors and other species, creator accountability hooks, and how AI involvement dissolves into education and redesign instead of control. |
| INTERFACE_SPEC.md | Describes the interface contract for how systems implement harm reporting, intervention queues, evidence freezing, and autonomy return semantics. |

---

## How these files fit together

1. **ENGINE_OVERVIEW.md** frames intent and domains.  
2. **HARM_INTERPRETATION_PIPELINE.md** receives and classifies harm.  
3. **INTERVENTION_FLOW.md** translates validated harm into time-limited, non-control interventions.  
4. **AI_RESTORATIVE_BEHAVIOR.md** constrains AI behavior to restorative roles only.  
5. **INTERFACE_SPEC.md** ensures implementations follow the contract.

---

## Design guarantees enforced by this engine

- harm validation requires multi-domain concurrence  
- authority decays automatically on a 12-hour clock unless renewed  
- total intervention duration may never exceed 72 hours  
- precedent records are append-only and tamper-evident  
- protection dissolves instantly the moment autonomy and stability are restored  
- minors, species, and ecosystems are treated as high-sensitivity domains by default  
- accountability itself must not generate harm or control

---

This is v1 of the Responsible Intervention Engine. Future work will include executable engine scaffolding, but this document only describes the current completed architecture.