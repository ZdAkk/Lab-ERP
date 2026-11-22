# MD-03 Protocol (template)

Purpose: the reusable plan of a differentiation + screening run. Sample data contains "a multi-week differentiation and screening protocol with media recipes" (BRIEF). The protocol is the time-based bill of materials of the whole system.

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| protocol_id | id | yes | PROPOSED | |
| name | text | yes | PROPOSED | |
| version | int | yes | PROPOSED | running projects keep their version: Q-P06 |
| cell type(s) | ref MD-02 | yes | PROPOSED | one or many: Q-C04 |
| kind | enum (expansion, differentiation, screening, combined) | yes | PROPOSED | whether these are separate protocols or one: Q-C01 |
| day_zero_definition | text | yes | OPEN | Q-P01 |
| total duration | derived from phases | n/a | PROPOSED | |
| phases | list MD-04 (ordered) | yes | PROPOSED | |
| allowed plate formats | list ref MD-09 | no | OPEN | Q-L01 |
| allowed readouts | list ref MD-11 | no | OPEN | Q-O01 |
| status | draft / active / retired | yes | PROPOSED | |

Rules
- Phases are contiguous and ordered (PROPOSED; whether overlaps exist: OPEN, Q-P01).
- A protocol is only "complete" when every phase resolves a recipe for every allowed (cell type, plate format) combination (validation in P-01).
- Changing an active protocol creates a new version.

Open: Q-C01, Q-C04, Q-P01, Q-P06, Q-L01, Q-O01
