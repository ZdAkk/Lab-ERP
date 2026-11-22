# 06 Status models (all PROPOSED)

States and transitions are proposals so the system has a lifecycle. Domain expert / Systasy confirm which are real.

## Screen project (TD-01)
draft → calculated → quoted → accepted → released (scheduled, stock reserved, devices booked) → running → completed
- any state before running → cancelled
- running → on_hold (OPEN: is replanning in scope, Q-PL03)
- Recalculation allowed in draft/calculated/quoted. From accepted on, master data is frozen via snapshots.

## Quote (TD-10)
draft → sent → accepted | rejected | expired (validity date, as standard ERP sales offer)

## Task (TD-04)
planned → due → done | skipped | deviated (with note)

## Media preparation (TD-05)
planned → prepared → in_use → used_up | expired | discarded

## Stock lot (TD-06)
received → (released, if QC exists: OPEN) → opened → consumed | expired | discarded

## Order list line (TD-08)
proposed → accepted → on_po (linked PO item) → received
- PO itself keeps standard ERP states (confirmed, locked, partially/fully received, cancelled)

## Device booking (TD-09)
tentative (created by plan) → confirmed (project released) → cancelled

## Calculation run (TD-12)
running → succeeded | failed (with validation errors). Each run is immutable.
