# TD-07 Reservation

Based on standard ERP reservations (from physical stock, incoming PO supply, or mixed). Change: reservations are time-phased (need date) and belong to a project/task, not a sales order.

| Field | Status |
|---|---|
| reservation_id | PROPOSED |
| project_id, task_id or preparation_id | PROPOSED |
| material | PROPOSED |
| quantity | PROPOSED |
| need date | NEW, PROPOSED |
| source: lot_id OR po_item_id | standard ERP pattern |
| status (soft = calculated, hard = project released) | PROPOSED |

Rules
- Soft reservations exist only in a calculation run (what-if for quotes). Hard reservations are created at project release (P-09) and block stock for other projects (if Q-M05 = yes).
