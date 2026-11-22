# 03 Input form (screen request)

Building block 1. Fields named in the brief are BRIEF. Everything else is PROPOSED or OPEN. The form creates a TD-01 Screen Project in status `draft`.

## Fields

| # | Field | Type | Status | Notes |
|---|---|---|---|---|
| F01 | Project name / reference | text | PROPOSED | |
| F02 | Customer | ref MD-13 | PROPOSED | optional for internal screens |
| F03 | Cell type(s) | ref MD-02, multi? | BRIEF | one or several per project: Q-G04 |
| F04 | Cell line(s) | ref MD-01, multi | PROPOSED | brief says "cell types"; whether line is a separate input: Q-C03 |
| F05 | Protocol | ref MD-03 | PROPOSED | may be derived from cell type: Q-C04 |
| F06 | Plate format | ref MD-09 | BRIEF ("plates and format") | |
| F07 | Number of plates OR derived | int | BRIEF ("plates") | entered directly, or derived from substances x conditions x replicates / wells per plate: Q-L03 |
| F08 | Substances | list of ref MD-10 + per-substance concentrations | BRIEF | concentrations / dose points: Q-L03 |
| F09 | Replicates | int | BRIEF | replicate level (wells, plates, batches): Q-L03 |
| F10 | Controls | config | OPEN | Q-L02 |
| F11 | Readouts | multi ref MD-11 | BRIEF | |
| F12 | Desired date | date | BRIEF | meaning (start / readout / delivery of results): Q-PL01 |
| F13 | Date mode | enum | PROPOSED | `backward_from_delivery` (brief) or `forward_from_start` |
| F14 | Earliest possible start | date | PROPOSED | default today; used for feasibility warning |
| F15 | Planning options | flags | OPEN | e.g. weekend work allowed: Q-W01 |
| F16 | Treatment timepoint(s) | config | OPEN | Q-S03 |

## Derived (shown live, not entered)
- total conditions, total wells, total plates, plates per batch, number of batches (PROPOSED formulas in E-01, inputs OPEN)
- earliest feasible delivery date
- first warnings (missing master data, infeasible date)

## Validation rules (PROPOSED)
- V1 plate format must be allowed for the chosen protocol/readout (allowed combinations OPEN: Q-L01)
- V2 every referenced substance needs the fields required by E-02 (stock concentration etc., Q-S02)
- V3 wells needed must fit plate capacity after layout rules (Q-L02)

## Defaults
None invented. Defaults are configured in MD-17 once known.
