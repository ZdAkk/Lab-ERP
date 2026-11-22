# E-01 Engine pipeline

Input: request (TD-01 params), master data snapshot, stock snapshot (lots, open POs, other reservations), settings (MD-17), today.
Output: layout, tasks, preparations, demand, order list, bookings, conflicts, costs, trace.

| Stage | Process | Spec | Key outputs |
|---|---|---|---|
| 0 Validate | P-02 | 03 V1-V3 + completeness checks | errors (stop) / warnings |
| 1 Layout | P-03 | R-06 | conditions, wells, plates, batches |
| 2 Schedule | P-04 | E-04 | tasks with dates |
| 3 Media | P-05 | E-02 | events, preparations, component amounts |
| 4 Materials | P-06 | E-03 | demand lines, allocation, order list |
| 5 Devices | P-08 | E-05 (capacity rules) | bookings |
| 6 Conflicts | all | E-05 | conflict list |
| 7 Costs | P-09 | E-06 | cost lines, per plate/batch/project |

Iteration: stage 4 produces order-by dates that feed back into stage 2 feasibility (one extra pass, PROPOSED). No optimizer in v1: the engine plans deterministically and warns; resolving conflicts is the user's decision (PROPOSED; operations research optimization is a later step, Systasy suggested OR as a discipline).

Every stage writes trace nodes (E-07).
