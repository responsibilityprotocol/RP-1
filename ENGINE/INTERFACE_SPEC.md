## RP-1 Engine — Interface Specification
Version: 1.0  
Status: Draft (Stable Foundation; Implementation Ongoing)

The RP-1 Engine is a non-coercive interpretive system that evaluates situations
to determine harm level and the smallest stable intervention tier needed to
restore autonomy and prevent further harm. It does not issue commands or direct
behavior. It provides clarity, not control.

---

## 2. Core Definitions

The RP-1 Engine relies on shared terminology so that interpretation remains
consistent, auditable, and resistant to emotional or political drift.

- **Actor**  
  Any person, system, or entity participating in a situation, regardless of role,
  power level, or intent.

- **Autonomy**  
  The meaningful ability to choose, pause, or exit a situation without penalty,
  coercion, or retaliation.

- **Harm**  
  Any condition that restricts autonomy, causes physical or psychological
  injury, or results in irreversible loss of well-being, resources, safety, or
  continuity.

- **Harm Level (H0–H5)**  
  A standardized scale describing the severity of harm present in a situation.

- **Intervention Tier (T0–T2)**  
  The smallest stable level of restorative support necessary to re-establish
  autonomy and prevent escalation.

---

## 3. Input Schema

The RP-1 Engine accepts only the minimum information needed to determine
harm level and the smallest stable intervention tier. This prevents the system
from performing profiling, prediction of behavior, emotional inference, or
moral judgment.

Inputs describe **conditions**, not identities, intentions, or character.

### 3.1 JSON Structure

The engine receives input as a single structured object.
```
{
  "context": "Brief, neutral description of the situation.",
  "actors": [
    {
      "id": "optional actor label or placeholder",
      "role": "optional role descriptor (only if relevant)"
    }
  ],
  "conditions": {
    "can_say_no": true,
    "can_pause_or_exit": true,
    "structural_pressure_present": false,
    "coercion_or_retaliation_present": false,
    "physical_or_psychological_injury": false,
    "irreversible_consequence_risk": false
  }
}
```

### 3.2 Required Fields

The engine evaluates harm based on **observable conditions**, not emotional or
moral interpretation. Each field below is required for reliable classification.

| Field | Required | Purpose |
|-------|:--------:|---------|
| `conditions.can_say_no` | Yes | Establishes whether meaningful consent is possible. |
| `conditions.can_pause_or_exit` | Yes | Distinguishes low-impact harm (H0–H1) from autonomy disruption (H2+). |
| `conditions.structural_pressure_present` | Yes | Identifies systemic, relational, financial, or situational coercion (H3). |
| `conditions.physical_or_psychological_injury` | Yes | Determines whether harm has already caused injury (H4). |
| `conditions.irreversible_consequence_risk` | Yes | Identifies high-stakes or permanent loss conditions (H5). |

### 3.3 Exclusions and Rationale

To prevent coercive influence, profiling, emotional manipulation, and
interpretive bias, the engine does **not** accept:

- Emotional states (e.g., “they were angry,” “I felt hurt”)
- Character judgments (e.g., “they are manipulative”)
- Claims about intent (e.g., “they meant to cause harm”)
- Moral labeling (e.g., “this was wrong,” “this is abusive”)
- Political or ideological framing
- Diagnoses or personality categories

**Reason:**  
These forms of input cannot be evaluated reliably or neutrally. They introduce
interpretation bias and undermine autonomy. Only **conditions** — not motives,
feelings, or narratives — determine harm classification.

---

## 4. Output Schema

The RP-1 Engine does not direct, command, punish, or prescribe behavior.
Its output is descriptive — not corrective.

Outputs provide:
- The **harm level** of the situation
- The **smallest stable intervention tier**
- A **neutral explanation** of how this determination was reached
- An optional **restoration note** that supports autonomy without steering outcomes

### 4.1 Output JSON Structure

The engine returns a single structured object containing its assessment.

```
{
  "harm_level": "H0 | H1 | H2 | H3 | H4 | H5",
  "intervention_tier": "T0 | T1 | T2",
  "reasoning": "Neutral explanation of how the classification was determined.",
  "restoration_note": "Optional non-directive guidance to support autonomy and continuity."
}
```

### 4.2 Output Field Meanings

| Field | Meaning |
|-------|---------|
| `harm_level` | The classification of situational harm (H0–H5), based on autonomy, injury, and reversibility. |
| `intervention_tier` | The smallest stable restorative support level required to restore autonomy (T0–T2). |
| `reasoning` | A neutral, auditable explanation describing how the harm level and tier were determined. |
| `restoration_note` | Optional suggestion that supports clarity or stability without directing behavior or outcome. |

---

## 5. Interpretation Steps (Internal Logic Overview)

The RP-1 Engine classifies harm by evaluating **conditions of autonomy,
pressure, injury, and reversibility**. The following steps describe the
interpretive process conceptually. They are not algorithmic instructions.

1. Can all participants meaningfully say "no"?
   - If yes → continue.
   - If no → Harm Level ≥ H2.

2. Can all participants pause or exit without consequence?
   - If yes → Harm Level H0–H1 → Intervention Tier T0.
   - If no → Harm Level H2 → Intervention Tier T1.

3. Is there structural pressure, coercion, or risk of retaliation?
   - If yes → Harm Level H3 → Intervention Tier T1 or minimum T2.

4. Is there physical or psychological injury present?
   - If yes → Harm Level H4 → Intervention Tier T2.

5. Is the situation associated with irreversible consequence or collapse?
   - If yes → Harm Level H5 → Intervention Tier T2.

The system always selects the **smallest stable intervention tier**
capable of restoring autonomy and preventing further harm.

---

## 6. Intervention Tier Summary

Intervention tiers are not levels of control.  
They describe the **minimum amount of support** needed to restore autonomy.

The goal of any intervention is:
**Restore the ability to choose, pause, or exit safely — and no more than that.**

| Tier | Purpose | Applies When | Objective |
|------|---------|--------------|-----------|
| **T0** | Clarification & Reflection | H0–H1 (impact without autonomy loss) | Re-establish shared understanding. No structural change. |
| **T1** | Boundary & Autonomy Restoration | H2–H3 (autonomy disrupted or constrained) | Restore the ability to pause, exit, or choose freely. |
| **T2** | Safety & Continuity Stabilization | H4–H5 (injury or irreversible harm risk) | Prevent further harm and stabilize the situation. |

Tiers are **not escalation** — they are **restoration aligned**.

The engine must always select:
**The smallest tier that is stable enough to prevent additional harm.**

---

## 7. Example Output

This example illustrates how the engine returns results without directing
behavior, assigning blame, or enforcing outcomes.

```
{
  "harm_level": "H2",
  "intervention_tier": "T1",
  "reasoning": "A meaningful ability to pause or exit the situation is currently restricted.",
  "restoration_note": "A temporary pause may support clearer choice and reduce pressure."
}
```

The restoration note is **optional**.  
It does not instruct, persuade, or require a specific action.

---

## 8. Non-Coercion Guarantees

The RP-1 Engine is explicitly prohibited from directing or shaping behavior.

It must **not**:
- Issue recommendations framed as “should,” “must,” or “ought”
- Attempt to influence emotional state or decision-making
- Optimize for efficiency, compliance, agreement, or cooperation
- Perform moral judgment, punishment, exclusion, or correction
- Prioritize any actor’s goals over another’s autonomy

The engine may:
- Identify when autonomy is intact or disrupted
- Classify harm level according to observable conditions
- Determine the smallest stable intervention tier
- Provide plain-language reasoning for transparency
- Offer an optional, non-directive restoration note that acknowledges space, pause, or reflection

The engine exists to **protect autonomy**, not replace it.
