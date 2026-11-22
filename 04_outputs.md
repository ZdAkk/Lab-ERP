# 04 Outputs

All outputs are produced from one calculation run (TD-12 calculation trace) and are reproducible from the same inputs + master data version.

| ID | Output | Building block | Content | Status |
|---|---|---|---|---|
| O1 | Media plan | 2 | per day: which recipe, which plates, volume needed, which preparation covers it | BRIEF |
| O2 | Recipe sheets | 2 | per media preparation: component amounts (volume/mass), base medium volume, prep date, expiry ("use by") | BRIEF (volumes, additives, shelf life) |
| O3 | Project plan | 3 | daily task list + timeline (Gantt) from start to delivery, backward planned | BRIEF |
| O4 | Conflict list | 3 | warnings with severity, date, cause, affected task, suggested fix | BRIEF; rule set in E-05 |
| O5 | Order list | 4 | per material: gross need, stock on hand (usable at need date), reserved, net need, packs to order, order-by date, supplier, price | BRIEF ("checked against stock") |
| O6 | Device bookings | 4 | per device: time slots requested; overlaps flagged | BRIEF |
| O7 | LIMS export | 4 | sample/plate list in LIMS import format | BRIEF; format OPEN (Q-I01) |
| O8 | Cost sheet | 5 | cost per plate, per batch, per project, split by cost type | BRIEF; components OPEN (Q-K01) |
| O9 | Quote document | 5 | customer facing price document | PROPOSED; content OPEN (Q-K05) |
| O10 | Reference comparison | success | our numbers vs reference, line by line, with deltas | PROPOSED (critical for the demo) |
| O11 | Calculation trace | all | every intermediate number with formula and inputs | PROPOSED |

## Formats (PROPOSED)
- Screen views in the app, CSV/XLSX export for O1, O2, O5, O8, PDF for O2 and O9 (standard ERP already generates PDFs).
- O10 as a table with green/red per line. This is the slide that proves "success" at the pitch.
