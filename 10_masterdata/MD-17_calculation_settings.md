# MD-17 Calculation settings

Purpose: global parameters of the engine, configurable in a settings section (as standard ERP settings), so the engine can be aligned to the reference without code changes. All values OPEN until the reference calculation is seen.

| Setting | Type | Status | Question |
|---|---|---|---|
| overage on media volume | % and/or absolute per prep | OPEN | Q-R06 |
| dead volume per plate / reservoir | volume | OPEN | Q-R06 |
| rounding of component amounts | decimals / step size per unit | OPEN | Q-G03 |
| rounding of prep volumes to standard sizes | rule | OPEN | Q-R05 |
| prep grouping strategy | one prep per feeding / max days by shelf life / fixed weekly | OPEN | Q-R05 |
| pack rounding | always up / allow partial | OPEN | Q-M04 |
| charge opened-pack remainder to project | bool | OPEN | Q-K02 |
| extra plates (spare) | int or % | OPEN | Q-L04 |
| stock allocation rule | FEFO / FIFO | OPEN | Q-M02 |
| consider other projects' reservations | bool | OPEN | Q-M05 |
| weekend handling | warn / shift earlier / shift later | OPEN | Q-W01, Q-P04 |
| today's date | input per run | PROPOSED | determinism |
| currency | | OPEN | Q-K04 |
