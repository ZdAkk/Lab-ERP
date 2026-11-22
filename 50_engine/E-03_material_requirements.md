# E-03 Material requirements and netting spec

## Demand sources
1. preparation components (E-02)
2. at_use components (E-02 §5)
3. step resource materials: qty × basis multiplier (per well/plate/batch/project/event) (R-08)
4. readout materials (R-09)
5. consumables if counted (Q-M03)

## Consumption granularity (OPEN whether used, Q-K02, Q-R04)
If a material is consumed from aliquots or packs that expire after opening, actual consumption = number of units opened × unit size, not the exact amount. Engine computes both: exact need and opened-unit need; setting chooses which one feeds order list and cost.

## Netting (per material, by need date ascending)
1. usable lots: expiry ≥ need date (check variant: Q-M02), minus reservations of other projects (Q-M05), allocate FEFO/FIFO.
2. incoming PO items with ETA ≤ need date.
3. remainder = net need.

## Order list
- packs = ceil(net need / pack size) (rounding: Q-M04), respecting MOQ.
- order-by = earliest uncovered need date − lead time (− buffer OPEN).
- If shelf life is short relative to the project, split into several orders by need date (OPEN, Q-M04/Q-R04).

## Outputs
O5 order list, soft reservations, conflict inputs (C-03, C-05).
