# TD-08 Order list and purchase order

## Order list line (new)
| Field | Status | Notes |
|---|---|---|
| material, supplier article | PROPOSED | preferred article from MD-08 |
| gross need (sum over project) | BRIEF | |
| usable stock at need date | BRIEF ("checked against stock") | expiry aware |
| reserved by others | OPEN | Q-M05 |
| incoming (open PO) | PROPOSED | standard ERP has incoming supply |
| net need | BRIEF | |
| packs to order, order quantity | PROPOSED | pack rounding: Q-M04 |
| first need date | PROPOSED | |
| order-by date | PROPOSED | = first need date − lead time (− buffer OPEN) |
| price, line total | BRIEF (material prices) | |
| status | see 06 | PROPOSED |

## Purchase order
Reuse standard ERP PO as is: grouping order lines by supplier creates a PO (items, confirmation, lock, shipments, goods receipt → lot).

Rules
- Time-phased netting: a material needed in week 2 and week 9 may need two orders if shelf life is short (OPEN whether reference does this: Q-M04, Q-R04).
