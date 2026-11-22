# MD-01 Cell line (iPSC line)

Purpose: the starting cell material. Systasy works with patient-derived and healthy donor iPSC lines (BRIEF, website).

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| cell_line_id | id | yes | PROPOSED | |
| code | text, unique | yes | PROPOSED | internal line name |
| donor_type | enum (patient, healthy, other) | no | BRIEF (website mentions both) | values OPEN |
| disease / indication | text | no | BRIEF (website lists disease areas) | |
| genotype / modification | text | no | OPEN | e.g. reporter or edited lines: Q-C03 |
| source | enum (own, purchased, partner) | no | OPEN | Q-C02 |
| passage limits | int | no | OPEN | Q-C03 |
| expansion protocol | ref MD-03 | no | OPEN | only if expansion is planned: Q-C01 |
| cryo stock (vials available) | derived from TD-06? | no | OPEN | are frozen vials tracked as stock: Q-C01 |
| data protection class | enum | no | OPEN | donor data includes clinical data on the website; the challenge data is non-critical |
| active | bool | yes | PROPOSED | |

Rules
- A cell line can be differentiated into one or more cell types (relation R-05). Whether every line works with every protocol: OPEN (Q-C04).

Open: Q-C01, Q-C02, Q-C03, Q-C04
