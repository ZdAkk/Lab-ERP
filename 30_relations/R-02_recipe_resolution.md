# R-02 Recipe resolution: (phase, cell type, plate format) → recipe

Brief: recipes differ "per phase, plate format and cell type". Modeled as a rule table so a missing combination is detectable.

| phase | cell type | plate format | recipe |
|---|---|---|---|
| required | required or ANY | required or ANY | required |

Rules (PROPOSED)
- Most specific match wins (exact > ANY).
- No match → validation error before calculation (never a silent default).
- If plate format only changes volume, not composition (Q-R01), plate format is always ANY and volume comes from MD-09.

Open: Q-R01, Q-C04
