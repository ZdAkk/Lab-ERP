# P-08 Device booking and capacity check

Building block 4 (device calendar). Engine stage 5.

Steps
1. From tasks, generate device demand (R-08, R-09): time demand per task, space demand (incubator plate slots) per batch over the run.
2. Assign concrete devices of the required type (first free, PROPOSED).
3. Check against existing confirmed bookings and capacity (Q-D01).
4. Flag overlaps (C-04) and over-capacity (C-06).
5. On project release: tentative bookings become confirmed; optional export to an external calendar (Q-D03).

Output: TD-09 bookings, calendar view (O6), conflicts.
