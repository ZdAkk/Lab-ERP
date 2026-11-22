# MD-09 Plate format

Purpose: defines wells and volumes, so the engine can scale everything per well. 96- and 384-well are named for pathwayPROFILER on the Systasy website (BRIEF).

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| plate_format_id | id | yes | PROPOSED | |
| name | text | yes | BRIEF | e.g. "96-well", "384-well" |
| rows x columns, total wells | int | yes | PROPOSED | derived from format |
| usable wells | int or layout rule | yes | OPEN | edge wells excluded?: Q-L02 |
| working volume per well | volume, possibly per phase | yes | OPEN | Q-L01 |
| surface area per well | area | no | OPEN | only if coating/seeding scale by area |
| plate material | ref MD-07 (the plate as consumable) | no | PROPOSED | Q-M03 |
| coating required | bool / ref | no | OPEN | Q-P03 |
| other vessels | flasks, 6-well for expansion | no | OPEN | same entity "vessel type" if expansion is in scope: Q-C01 |

Rules
- Total wells per project = f(conditions, replicates, controls, layout rules); formula in E-01, rules OPEN.

Open: Q-L01, Q-L02, Q-C01, Q-M03, Q-P03
