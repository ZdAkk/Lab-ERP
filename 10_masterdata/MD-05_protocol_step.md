# MD-05 Protocol step (task template)

Purpose: an action on protocol days. Generates TD-04 tasks, device demand, material consumption and labour.

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| step_id | id | yes | PROPOSED | |
| phase_id | ref MD-04 | yes | PROPOSED | |
| step_type | enum | yes | PROPOSED | candidate values: coating, seeding, feeding, replating, transduction, treatment, lysis, fixation, imaging, readout, freezing. Real list OPEN: Q-P03 |
| day pattern | explicit days OR every n days OR weekdays | yes | PROPOSED | Q-P02 |
| time window | allowed shift in days (earlier/later) | no | OPEN | Q-P04 (decides how conflicts are resolved) |
| exchange fraction | decimal (feeding only) | cond. | OPEN | full vs partial media change: Q-P02 |
| volume basis | per well from MD-09 or explicit | cond. | OPEN | Q-L01 |
| uses recipe | yes/no | yes | PROPOSED | feeding uses phase recipe; other steps may use other materials |
| step materials | list (material, quantity, basis: per well / per plate / per batch / per project) | no | PROPOSED | e.g. coating solution, plates, tips. Content OPEN: Q-M03 |
| devices | list (device type, duration, basis) | no | PROPOSED | Q-D02 |
| hands-on time | duration + basis | no | OPEN | Q-P05 |
| external service | ref (e.g. sequencing) | no | OPEN | Q-O02 |
| depends on | previous step + min/max gap | no | PROPOSED | for scheduling precedence |

Rules
- Quantity basis is explicit on every resource line so the engine can scale: per well, per plate, per batch, per project, per preparation. (PROPOSED; the reference may use only some.)
- Readout-specific steps come from MD-11 and are appended to the project schedule (R-09).

Open: Q-P02, Q-P03, Q-P04, Q-P05, Q-D02, Q-M03, Q-O02
