# 08 MVP plan until the pitch (Fri 27.11.2026, 17:00, Kleine Aula)

## Scope proposal (decide in Q-G01)
Must (the reference match): blocks 1, 2, 5 and the order list part of 4.
Should: block 3 (backward plan + conflicts C-01 to C-07).
Could: device calendar view, LIMS CSV export, quote PDF.
Won't (story only): execution tracking (P-10), replanning, integrations.

Reason: success is measured against the reference calculation. The media → materials → cost chain is what it most likely contains (Q-G03). Scheduling is visible and impressive but only scores if the reference includes dates.

## Steps
| # | When | What | Who (proposal) |
|---|---|---|---|
| 1 | Sat, now | Domain expert reviews 90_open_questions + master data; mark answers / "in sample data" | Olga / Michael with Zaid |
| 2 | Sat | Send top 10 questions to Sven Wichert (email comes Monday per brief, ask at kick-off if possible) | Anna / Daniel |
| 3 | Sat build time | Receive sample data, P-01 import mapping; encode reference as fixture (P-12) | Zaid + Olga |
| 4 | Sat evening to Sun | Engine stages 0, 1, 3, 4, 7 (layout, media, materials, cost) + trace, test against fixture until green | Zaid (engine), Olga (checks recipes) |
| 5 | Mon to Tue | Stage 2 schedule + conflicts; UI: input form, results tabs (media plan, recipe sheets, order list, costs, plan), reference comparison table | Zaid + Olga |
| 6 | Mon to Wed | Customer validation: talk to Systasy lab staff and 3 to 5 other labs; LOI from Systasy for a pilot | Daniel + Anna |
| 7 | Wed 25.11. co-working | Demo dry run, pitch practice, polish | all |
| 8 | Fri 27.11. | 5 min pitch incl. live demo: enter request → full plan in seconds → green reference match | all |

## Tech
- Reuse the standard ERP foundation (same stack, master data UI, purchasing, stock, audit).
- Engine as a separate pure module with fixture tests.
- Hosting like standard ERP (dev/staging/prod not needed for the demo: one environment).

## Pitch Pass mapping
1 Problem: hours per quote, batch losses from calculation errors or missing reagents (BRIEF).
2 Proof: reference match + time saved per quote, statement from Systasy.
3 Commitment: pilot / LOI with Systasy, further labs from customer validation.

## Risks
- Sample data late or very different from this model → the open fields absorb it; adjust MD-17 settings, not code.
- Reference has hidden conventions (rounding, overage) → trace + configurable rounding points.
- Scope creep into scheduling optimization → v1 warns only, no optimizer.
