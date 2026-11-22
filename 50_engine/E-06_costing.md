# E-06 Costing spec

## Cost lines
| Type | Quantity source | Price source | Status |
|---|---|---|---|
| material | E-03 consumption (exact or opened units, Q-K02) | supplier article: pack price / pack size | BRIEF (material prices) |
| consumable | step resources | supplier article | OPEN (Q-M03) |
| labour | hands-on time from tasks | MD-15 labour rate | OPEN (Q-K01, Q-P05) |
| device | booking hours / plate-days | MD-15 device rate | OPEN (Q-K01) |
| external | samples × readout service price | MD-11 / MD-15 | OPEN (Q-O02) |
| overhead | % or fixed | MD-15 | OPEN |
| margin | % (quote only) | MD-15 | OPEN |

## Allocation (BRIEF: per plate, batch, project)
- plate-level lines: directly on the plate (e.g. plate consumable, per-well materials summed)
- batch-level lines: split over plates of the batch
- project-level lines: split over batches/plates
Split key (equal / by wells / by usage): OPEN (Q-K01). The engine stores the unallocated lines too so any key can be applied.

## Unit price rule
unit_price = pack_price / pack_size (in base unit), decimal, no rounding until the configured point (E-07).

## Outputs
O8 cost sheet: per plate, per batch, per project, split by type; O9 quote positions (Q-K05).
