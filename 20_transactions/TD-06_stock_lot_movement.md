# TD-06 Stock lot and stock movement

Based on standard ERP warehouse_stock (per batch: quantity_on_hand, reserved_quantity, available_quantity, received_date, po link) and movements (IN / OUT / ADJUSTMENT, reason_code, source links). Sample data contains "a sample stock" (BRIEF).

## Lot (new fields marked)
| Field | Status | Notes |
|---|---|---|
| lot_id, material, lot number | standard ERP | |
| quantity on hand / reserved / available | standard ERP | |
| received date, PO link | standard ERP | |
| expiry date | NEW, PROPOSED | Q-M02 |
| opened / thawed date | NEW, OPEN | Q-R04 |
| remaining in opened unit | NEW, OPEN | |
| storage location | NEW, OPEN | |
| QC status | NEW, OPEN | |

## Movement types
standard ERP: IN (goods receipt), OUT (delivery), ADJUSTMENT. New PROPOSED source types:
- OUT media_preparation, OUT task_consumption, OUT discard_expired, IN returned/aliquoted (OPEN)

Rules
- Stock usable for a need on date d = lots with expiry ≥ d (or ≥ d + use duration: OPEN, Q-M02).
- Allocation order FEFO/FIFO from MD-17.
