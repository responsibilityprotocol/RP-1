```markdown
```mermaid
flowchart TD

    A[Observed Action / Condition] --> B[Harm Assessment (H0-H5)]
    
    B -->|H0: No Harm| C[T0 Advisory Only]
    C --> R[End]

    B -->|H1-H2: Low/Moderate Harm| D[T1 Preventive Guidance]
    D --> E[Offer Correction + Support]
    E --> R

    B -->|H3-H4: Significant Harm| F[T1 or T2 Conditional Intervention]
    F --> G[Reversibility Check]
    G --> H[Due Process & Appeals]
    H --> R

    B -->|H5: Severe / Imminent Harm| I[T2 Emergency Override]
    I --> J[Immediate Harm Prevention]
    J --> H2[Mandatory Post-Action Review]
    H2 --> R