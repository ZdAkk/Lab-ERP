# TD-05 Media preparation

Purpose: one physical preparation of a recipe (e.g. one bottle) covering one or more feeding tasks until it expires. Brief: recipes "including volumes, additives and shelf life".

| Field | Type | Status | Notes |
|---|---|---|---|
| preparation_id | id | PROPOSED | |
| recipe | ref MD-06 (snapshot version) | BRIEF | |
| planned prep date | date | PROPOSED | |
| volume | volume | BRIEF | = sum of covered demand + overage, rounding OPEN (Q-R05, Q-R06) |
| expiry ("use by") | date | BRIEF (shelf life) | rule OPEN (Q-R04) |
| covered tasks | list TD-04 | PROPOSED | |
| component lines | material, calculated amount, unit, lot (when executed) | BRIEF (additives) | |
| status | see 06 | PROPOSED | |
| prepared by / at | | PROPOSED | execution |

Rules
- A preparation may only cover tasks whose date is ≤ expiry (E-02).
- Whether preparations are shared across projects using the same recipe: OPEN (Q-M05).
