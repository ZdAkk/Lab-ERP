# TD-03 Plate and well (layout)

## Plate
| Field | Type | Status |
|---|---|---|
| plate_id, plate_label | id, text | PROPOSED (label/barcode convention: Q-I02) |
| project_id, batch_id | ref | PROPOSED |
| plate format | ref MD-09 | BRIEF |
| cell line, cell type | ref | PROPOSED |
| is_spare | bool | OPEN (Q-L04) |
| lims sample id | ref TD-11 | OPEN |

## Well assignment
| Field | Type | Status |
|---|---|---|
| plate_id, well position (A1...) | | PROPOSED |
| role | enum (sample, vehicle_control, positive_control, untreated, empty, edge_excluded) | OPEN values (Q-L02) |
| substance, concentration | ref, decimal | BRIEF (substances) |
| replicate no | int | BRIEF |
| timepoint | | OPEN (Q-S03) |

Rules
- For the calculation, an explicit well map is only needed if the reference depends on it. Minimum needed: counts of wells and plates (E-01). Full layout map is PROPOSED as a later feature (and for LIMS export).
