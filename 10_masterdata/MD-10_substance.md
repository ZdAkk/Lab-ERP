# MD-10 Substance (test compound)

Purpose: compounds screened on the cells. Brief input: "substances".

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| substance_id | id | yes | PROPOSED | |
| name / code | text | yes | BRIEF | |
| owner / source | enum (customer_provided, purchased, internal library) | no | OPEN | Q-S01 |
| stock concentration + unit | decimal | cond. | OPEN | Q-S02 |
| solvent / vehicle | text or ref MD-07 | no | OPEN | Q-S02 |
| max solvent fraction per well | decimal | no | OPEN | Q-S02 |
| linked material | ref MD-07 | no | PROPOSED | if stocked and costed |
| molecular weight | decimal | no | OPEN | only if mass to molar conversion needed |

Per project (not master data, lives on TD-01): concentrations / dose points, timepoints, replicates.

Open: Q-S01, Q-S02, Q-S03, Q-L03
