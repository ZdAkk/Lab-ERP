# MD-06 Media recipe (+ recipe components)

Purpose: composition of a complete medium. Brief: "dozens of media recipes per phase, plate format and cell type", "volumes, additives and shelf life".

## Recipe header

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| recipe_id | id | yes | PROPOSED | |
| name / code | text | yes | PROPOSED | as named in sample protocol |
| version | int | yes | PROPOSED | |
| base medium | ref MD-07 | yes | PROPOSED | "fill up to volume" semantics: Q-R07 |
| shelf life after preparation | duration | yes | BRIEF (concept) | value OPEN: Q-R04 |
| storage condition | enum | no | OPEN | Q-R04 |
| standard prep sizes | list of volumes | no | OPEN | Q-R05 |
| applies to | (phase, cell type, plate format) via R-02 | yes | BRIEF | whether plate format changes composition: Q-R01 |

## Recipe component (line)

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| component_id | id | yes | PROPOSED | |
| recipe_id | ref | yes | PROPOSED | |
| material | ref MD-07 | yes | BRIEF ("additives") | |
| spec_type | enum (final_concentration, dilution_factor, amount_per_volume, percent_v_v, fill_to_volume) | yes | PROPOSED | which forms appear in sample data: Q-R02 |
| spec_value + unit | decimal + unit | yes | OPEN values | |
| stock concentration used | from MD-07 or override | cond. | OPEN | Q-R02 |
| add_timing | enum (at_preparation, at_use) | yes | PROPOSED | Q-R03; changes shelf life logic |
| own shelf life after thaw/open | duration | no | OPEN | Q-R04 |
| sequence | int | no | PROPOSED | for recipe sheet print |

Rules
- Component amount for a preparation volume V is computed in E-02 by spec_type. No formula is assumed beyond standard dilution math until the sample data shows the convention.
- Effective expiry of a preparation = min(recipe shelf life from prep, remaining life of every lot used) (PROPOSED; confirm: Q-R04).
- If add_timing = at_use, the component is not in the bottle; it creates its own demand at each feeding event (PROPOSED).

Open: Q-R01 to Q-R07
