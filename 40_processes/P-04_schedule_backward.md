# P-04 Schedule generation (backward planning)

Building block 3. Engine stage 2 (spec E-04).

Steps
1. Determine anchor: desired date and its meaning (Q-PL01). If it is the result delivery date, subtract readout time-to-data and analysis/report time (Q-O01, Q-PL01).
2. Place the last step (readout) on the latest allowed working day ≤ anchor.
3. Walk protocol backwards: each step placed at its protocol day offset relative to Day 0; Day 0 date = readout date − readout protocol day.
4. Apply calendar: if a step lands on a non-working day, apply the rule (shift within window / warn) (Q-W01, Q-P04).
5. Per batch, offset start dates if batches are staggered (Q-K03).
6. Prepend preparation lead steps: media preparation days, coating, cell thaw/expansion if in scope (Q-C01).
7. Prepend procurement: order-by dates from lead times (computed after P-06, iteration 2).
8. Check feasibility: earliest required action ≥ today (else conflict C-01).

Output: TD-04 tasks with dates, project start date, conflicts.
