# TD-01 Screen project

Purpose: one customer or internal screen. Holds the request (input form) and links all generated data.

| Field | Type | Status | Notes |
|---|---|---|---|
| project_id, project_number | id, text | PROPOSED | |
| status | see 06 | PROPOSED | |
| customer | ref MD-13 + snapshot | PROPOSED | |
| request parameters | all fields of 03_input_form | BRIEF/PROPOSED | stored as entered |
| conditions | list (substance, concentration, timepoint?) | PROPOSED | Q-L03 |
| replicates | int | BRIEF | Q-L03 |
| controls | config | OPEN | Q-L02 |
| desired date + mode | date, enum | BRIEF | Q-PL01 |
| protocol snapshot | frozen protocol + recipes version | PROPOSED | taken at acceptance |
| current calculation run | ref TD-12 | PROPOSED | |
| accepted quote | ref TD-10 | PROPOSED | |
| planned start / end | dates | PROPOSED | from engine |
| notes | text | PROPOSED | |

Children: TD-02 batches, TD-03 plates, TD-04 tasks, TD-05 preparations, TD-07 reservations, TD-08 order lines, TD-09 bookings, TD-10 cost calculation, TD-11 LIMS samples.
