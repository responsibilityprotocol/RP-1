# RP-1 Engine — Interface Specification

The RP-1 Engine is a reasoning support system designed to help humans, organizations, and artificial intelligence systems apply the RP-1 framework consistently. It provides interpretive guidance and proportionality validation while preserving autonomy and preventing coercion.

The Engine does **not** enforce compliance.  
It offers clarity — not correction or control.

---

## 1. Purpose

The Engine is designed to:
- **Interpret Harm (H0–H5)**
- **Recommend the smallest stable intervention (T0–T2)**
- **Support restoration and continuity**
- **Prevent unnecessary escalation or coercive behaviors**

The Engine is advisory-only and cannot override human or system decisions.

---
## 2. Core Functions

The RP-1 Engine performs two primary reasoning operations. Both are **interpretive** and **non-directive** — meaning they provide clarity and proportionality, not control or enforcement.

| Function | Name | Description |
|---------|------|-------------|
| Interpret Harm | `interpret_harm` | Evaluates the likely harm level involved in an interaction or decision (H0–H5) and explains the reasoning. |
| Recommend Intervention | `recommend_intervention` | Suggests the **smallest necessary** intervention tier (T0–T2) that aligns with the identified harm level. |

These functions:
- Do **not** require personal identity data
- Do **not** make moral or emotional judgments
- Must provide clear reasoning in plain language

Both functions are explicitly **non-coercive** and **non-authoritative**.

## 3. Input Schema

The Engine accepts minimal input to avoid dependence, coercion, or privacy intrusion.

### Input Format (Minimal Descriptive Input)

```json
{
  "event_description": "string (required)",
  "proposed_action": "string (optional)",
  "context": {
    "relationship": "string (optional)",
    "history": "string (optional)",
    "environment": "string (optional)"
  }
}

---
### Input Requirements & Safeguards

- `event_description` is the only required field.
- The Engine must **not** request:
  - Identity details
  - Personal psychological states
  - Emotional disclosure
  - Confession or justification
- `context` is optional and may be used only to:
  - Reduce misinterpretation
  - Understand communication structure
  - Avoid unnecessary escalation

The Engine must **never** use context to:
- Determine moral worth
- Assign blame
- Influence emotional response
- Infer intent beyond what is explicitly stated