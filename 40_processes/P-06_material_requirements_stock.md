# P-06 Material requirements and stock check

Building block 4 (order list). Engine stage 4 (spec E-03).

Steps
1. Collect demand lines: preparation components (P-05), at_use components, step resource materials (R-08), readout materials (R-09), consumables (Q-M03).
2. Convert to base units (MD-14). Account for consumption granularity (aliquots / opened packs with limited life → waste, Q-R04, Q-K02).
3. Sort demand by need date.
4. Allocate available lots (FEFO/FIFO, expiry ≥ need date, minus other projects' reservations if Q-M05).
5. Allocate open incoming PO quantities with ETA ≤ need date.
6. Remaining = net need per material and need date.
7. Order list: per material, round to packs (Q-M04), compute order-by date = first uncovered need date − lead time.
8. Conflicts: order-by date < today (C-03), expired lots needed (C-05).

Output: order list (O5), soft reservations, conflicts.
