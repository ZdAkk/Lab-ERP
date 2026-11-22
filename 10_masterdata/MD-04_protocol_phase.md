# MD-04 Protocol phase

Purpose: a time segment of a protocol with one media regime. Brief: recipes are calculated "per phase".

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| phase_id | id | yes | PROPOSED | |
| protocol_id | ref MD-03 | yes | PROPOSED | |
| sequence | int | yes | PROPOSED | |
| name | text | yes | PROPOSED | as in sample protocol |
| start_day / end_day | int (protocol days) | yes | PROPOSED | relative to Day 0: Q-P01 |
| duration variability | min/max days | no | OPEN | Q-P04 |
| feeding regime | ref to step pattern (MD-05) | yes | PROPOSED | frequency + exchange fraction: Q-P02 |
| recipe rule | via R-02 | yes | BRIEF | |
| working volume per well | via MD-09 or per phase | yes | OPEN | does volume change by phase: Q-L01 |
| vessel | plate format or expansion vessel | yes | OPEN | do early phases run in other vessels (flasks) before replating into screening plates: Q-P03 |
| quality gate at end | text | no | OPEN | job ad: "monitor differentiation quality" |

Rules
- Feeding events of a phase are generated from the step pattern (MD-05), not entered per day, unless the sample protocol lists explicit days (then explicit day list wins). Which one the sample data uses: OPEN (Q-P02).

Open: Q-P01, Q-P02, Q-P03, Q-P04, Q-L01
