# E-05 Conflict rules catalog

Brief asks for "conflict warnings" and states "a calculation error or a missing reagent can cost a whole batch". Rule list is PROPOSED; severity and which rules Systasy cares about: Q-PL02.

| ID | Rule | Detected in | Severity (PROPOSED) | Suggested fix shown |
|---|---|---|---|---|
| C-01 | Plan infeasible: required action before today | E-04 | error | earliest feasible delivery date |
| C-02 | Task on weekend/holiday without allowed shift | E-04 | warning | shift options within window |
| C-03 | Order-by date in the past (material will not arrive in time) | E-03 | error | alternative supplier / later start |
| C-04 | Device double booking with another project | P-08 | error | next free slot |
| C-05 | Required lot expires before use / preparation expires before last covered feeding | E-02, E-03 | error | split preparation / order fresh |
| C-06 | Device capacity exceeded (e.g. incubator plate slots) | P-08 | error | stagger batches |
| C-07 | Missing master data (no recipe for combination, no price, no unit) | stage 0 | error | link to master data record |
| C-08 | Stock reserved by another project needed here | E-03 | warning | show competing project |
| C-09 | Staff capacity exceeded on a day | E-04 | warning | OPEN, only if Q-W02 |
| C-10 | Too many tasks on one day (workload peak) | E-04 | info | OPEN threshold |
| C-11 | Solvent fraction above limit in treatment wells | P-03 | error | OPEN, only if Q-S02 |

Each conflict: id, severity, date, project, affected task/material/device, message, fix suggestion.
