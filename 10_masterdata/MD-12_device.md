# MD-12 Device (bookable resource)

Purpose: equipment that must be booked or has capacity. Sample data contains "a device list" (BRIEF).

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| device_id | id | yes | PROPOSED | |
| name | text | yes | BRIEF | |
| device type | enum / ref | yes | PROPOSED | steps reference types, engine assigns concrete devices |
| capacity model | enum (exclusive_time, parallel_slots, space_in_plates) | yes | PROPOSED | hood/liquid handler = time, incubator = plate space: Q-D01 |
| capacity value | int | cond. | OPEN | Q-D01 |
| booking granularity | minutes | no | OPEN | Q-D01 |
| availability calendar | ref MD-16 | no | PROPOSED | |
| hourly cost rate | money | no | OPEN | only if device time is costed: Q-K01 |
| location | text | no | PROPOSED | |
| external calendar id | text | no | OPEN | Q-D03 |

Rules
- Incubator space is a continuous demand over the whole run (plates occupy slots for weeks), while hood/imager demand is per task. Both must be modeled for conflict detection (E-05).

Open: Q-D01, Q-D02, Q-D03, Q-K01
