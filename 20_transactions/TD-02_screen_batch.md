# TD-02 Screen batch

Status: the whole entity is OPEN in meaning (Q-K03). The brief asks for "cost per plate, batch and project", so some grouping between plate and project exists.

Candidate meanings (to be decided by Systasy / domain expert, not by us):
- a) plates seeded / differentiated together on the same start day
- b) plates from one cell expansion / one cell line
- c) plates processed together in one readout run (e.g. one sequencing run)
- d) one replicate set

Proposed fields (valid for any meaning)

| Field | Type | Status |
|---|---|---|
| batch_id, batch_no | id, int | PROPOSED |
| project_id | ref | PROPOSED |
| start date (protocol Day 0) | date | PROPOSED, if meaning a) |
| plates | list TD-03 | PROPOSED |
| cell line | ref MD-01 | PROPOSED, if meaning b) |
| max plates per batch | from settings | OPEN (Q-L04) |

Why it matters: if batches are staggered in time (meaning a), the schedule, media preparations and device load change completely. Decide before building E-04.
