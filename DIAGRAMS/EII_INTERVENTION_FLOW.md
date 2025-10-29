# EII Intervention Flow Diagram

This flow represents how actions or conditions are assessed using the RP-1 Harm Scale (H0–H5), and how intervention tiers (T0–T2) are selected in accordance with reversibility, due process, and restoration principles.

```mermaid
flowchart TD

    A[Observed Action or Condition] --> B[Assess Harm Level (H0–H5)]

    %% No Harm
    B -->|H0: No Harm| C[T0 Advisory Only]
    C --> R[End]

    %% Low to Moderate Harm
    B -->|H1–H2: Low or Moderate Harm| D[T1 Preventive Guidance]
    D --> E[Education + Correction Support]
    E --> R

    %% Significant Harm
    B -->|H3–H4: Significant Harm| F[T1 or T2 Conditional Intervention]
    F --> G[Reversibility Check]
    G --> H[Due Process & Appeals]
    H --> R

    %% Severe or Imminent Harm
    B -->|H5: Severe / Imminent Harm| I[T2 Emergency Override]
    I --> J[Immediate Harm Prevention Action]
    J --> K[Mandatory Review + Restoration Path]
    K --> R

**Key Concepts Embedded in the Flow:**

| Harm Level | Meaning | Default Action |
|-----------|---------|----------------|
| **H0** | No harm present | Advice only (non-binding) |
| **H1–H2** | Mild to moderate harm | Preventive education + support |
| **H3–H4** | Clear or ongoing harm | Structured intervention with due process |
| **H5** | Imminent or severe harm | Emergency override + mandatory review |

This ensures:
- **Protection without domination**
- **Intervention is reversible whenever possible**
- **Emergency actions cannot become permanent**
- **Appeal pathways are always present**
- **Restoration is prioritized over punishment**
