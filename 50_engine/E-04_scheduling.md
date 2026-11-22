# E-04 Scheduling spec

## Anchor
- mode backward_from_delivery (BRIEF): T_delivery = desired date.
  T_readout = T_delivery − time_to_data(readout) − analysis/report time (Q-PL01, Q-O01).
- mode forward_from_start (PROPOSED): Day 0 = start date.

## Placement
date(step) = date(Day 0) + protocol_day(step); date(Day 0) = T_readout − protocol_day(readout step).
Per batch offset if staggered (Q-K03).

## Calendar rules
For each task on a non-working day (MD-16):
- if step window allows (Q-P04): shift to nearest allowed working day within window (direction preference in MD-17)
- else: keep and raise C-02 (weekend/holiday task)
Backward mode: if shifting the readout would move it earlier, recompute Day 0 so the whole chain stays consistent (PROPOSED; or shift only the single task: decided by Q-P04).

## Pre-steps
- media preparations placed on prep_date (E-02)
- procurement order-by dates (E-03)
- cell thaw / expansion if in scope (Q-C01)

## Feasibility
earliest_action_date = min(order-by dates, first task date). If < today → C-01 with the earliest feasible delivery date computed by forward run from today.

## Output
Tasks with dates and windows, project start/end, Gantt data (O3).
