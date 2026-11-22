# MD-02 Cell type

Purpose: the differentiated target cell. Website lists excitatory neurons, inhibitory neurons, sensory neurons, oligodendrocytes (BRIEF). Brief: recipes differ "per phase, plate format and cell type".

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| cell_type_id | id | yes | PROPOSED | |
| name | text, unique | yes | BRIEF | |
| default protocol | ref MD-03 | no | PROPOSED | if one protocol per cell type: Q-C04 |
| allowed plate formats | list ref MD-09 | no | OPEN | Q-L01 |
| 2D / 3D | enum | no | BRIEF (website: 2D and 3D models) | whether 3D (organoids) is in scope: OPEN |
| seeding density per plate format | quantity per well | no | OPEN | Q-C02, may live on MD-05 seeding step instead |
| co-culture | list of cell types | no | OPEN | not mentioned in brief |

Rules
- Recipe resolution uses (phase, cell type, plate format): see R-02.

Open: Q-C02, Q-C04, Q-L01, Q-R01
