# TD-10 Cost calculation and quote

## Cost line (from engine, E-06)
| Field | Status |
|---|---|
| cost type (material, consumable, labour, device, external, overhead, margin) | PROPOSED, used types OPEN (Q-K01) |
| source (material id, task id, readout id...) | PROPOSED |
| quantity, unit, unit price, amount | PROPOSED |
| allocation level (well, plate, batch, project) | BRIEF (plate, batch, project) |
| trace node id | PROPOSED |

Aggregates: cost per plate, batch, project (BRIEF). Allocation of project-level costs to plates: OPEN (equal split vs by usage, Q-K01).

## Quote (based on standard ERP sales offer)
| Field | Status |
|---|---|
| quote number, date, validity date, customer snapshot | standard ERP pattern |
| positions | OPEN (what the customer sees: Q-K05) |
| calculation run reference | PROPOSED |
| payment terms | standard ERP pattern |
| status | see 06 |
