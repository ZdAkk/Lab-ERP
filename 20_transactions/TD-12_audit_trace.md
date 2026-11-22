# TD-12 Audit and calculation trace

## Calculation run
| Field | Status |
|---|---|
| run_id, project_id, started_at | PROPOSED |
| input hash (request + master data versions + stock snapshot + settings + today) | PROPOSED |
| status succeeded / failed, validation errors | PROPOSED |
| outputs (all O1 to O8 as JSON) | PROPOSED |

## Trace node
| Field | Status |
|---|---|
| node id, label, value, unit | PROPOSED |
| formula (readable text) | PROPOSED |
| input node ids | PROPOSED |
| rounding applied | PROPOSED |
| reference value + delta (if reference loaded) | PROPOSED |

## Audit
Reuse standard ERP audit protocol for user actions and state changes (who, when, what, before/after).
