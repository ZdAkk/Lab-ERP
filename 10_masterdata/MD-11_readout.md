# MD-11 Readout (assay type)

Purpose: the measurement at the end. Brief input: "readouts". Systasy offers pathwayPROFILER (barcoded sensors, NGS readout), targetFinder, single cell / nucleus RNA sequencing, viral tropism profiling (BRIEF, website). Which ones apply to a screen: OPEN.

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| readout_id | id | yes | PROPOSED | |
| name | text | yes | BRIEF | |
| sample level | enum (well, pooled wells, plate) | yes | OPEN | drives sample count, NGS cost, LIMS rows: Q-O03 |
| added steps | list of MD-05 step templates with day offsets relative to treatment or protocol end | yes | PROPOSED | e.g. sensor introduction, lysis, RNA extraction: content OPEN Q-O02 |
| materials | list (material, qty, basis) | no | PROPOSED | Q-O02 |
| devices | list | no | PROPOSED | Q-D02 |
| external service | name, cost per sample, turnaround days | no | OPEN | in-house vs external sequencing: Q-O02 |
| time to data | days after sample taking | no | OPEN | needed for backward planning from delivery: Q-PL01 |
| compatible plate formats | list ref MD-09 | no | BRIEF partly (96/384 for pathwayPROFILER) | |

Rules
- A readout can add steps before the readout day (e.g. sensor delivery must happen before treatment). Placement uses offsets relative to an anchor step (PROPOSED).

Open: Q-O01, Q-O02, Q-O03, Q-PL01
