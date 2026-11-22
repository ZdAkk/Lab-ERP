# E-07 Rounding, units, trace and reference validation

## Numbers
- Decimal type for all quantities and money. No floats.
- Internal units: µL, µg, count, cents (PROPOSED).

## Rounding points (all configurable, values OPEN Q-G03)
R1 event volume, R2 preparation volume, R3 component amount (per unit type: pipettable step), R4 pack count (ceil), R5 unit price, R6 cost line amount, R7 aggregates.
Each rounding writes the pre- and post-value to the trace.

## Trace
See TD-12. Node ids are stable and human readable, e.g. `prep[phase2#3].component[B27].amount`, so they can be mapped to reference lines.

## Reference validation (P-12)
- Reference loaded as JSON fixture: { request, expected: [{ key, value, unit, tolerance? }] }.
- Mapping from reference line to trace node id maintained by hand (one-time).
- Tolerance default 0 (exact match); only allowed if Systasy says so.

## Determinism checklist
stable sort keys; today as input; no random ids in computed outputs; master data version pinned per run.
