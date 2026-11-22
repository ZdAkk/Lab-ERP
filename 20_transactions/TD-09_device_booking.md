# TD-09 Device booking

| Field | Status |
|---|---|
| booking_id | PROPOSED |
| device (concrete) or device type | PROPOSED |
| project_id, task_id | PROPOSED |
| start / end (or date + duration) | PROPOSED, granularity OPEN (Q-D01) |
| capacity used (time, slots, plate positions) | PROPOSED |
| status tentative / confirmed / cancelled | PROPOSED |
| external calendar event id | OPEN (Q-D03) |

Rules
- Incubator: one long booking per batch covering the whole run, capacity = plates.
- Time devices: one booking per task.
- Overlap with other projects' confirmed bookings → conflict C-04 (E-05).
