# P-07 Procurement (reuse standard ERP)

Trigger: project released or user accepts order list lines.

Steps (standard ERP flow)
1. Group accepted order lines by supplier → purchase order draft.
2. Send PO (mailto flow as in standard ERP), confirm, lock.
3. Track shipment, ETA.
4. Goods receipt: enter lot number + expiry date (new field) → lot created, movement IN.
5. Soft reservations on incoming PO convert to lot reservations.

Output: POs, lots, updated stock.
