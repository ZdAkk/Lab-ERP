# MD-14 Units and conversions

Purpose: correct dilution math and pack conversion. Errors here directly break the reference match.

| Field | Type | Status |
|---|---|---|
| unit code | text (mL, µL, L, mg, µg, g, ng, IU, pcs, pack, mM, µM, nM, ng/mL, µg/mL, %, x) | PROPOSED list, actual units from sample data |
| dimension | enum (volume, mass, amount, count, concentration_mass, concentration_molar, ratio, activity) | PROPOSED |
| factor to base unit | decimal | PROPOSED (standard SI factors) |

Rules
- Conversions only within a dimension. Mass to molar requires molecular weight (MD-10/MD-07), otherwise error, never silent.
- "x" (e.g. 50x supplement, use 1x) is a ratio unit: amount = V × target / stock (PROPOSED; confirm the sample data uses it this way: Q-R02).
- Activity units (IU) are not convertible to mass without a material-specific factor: OPEN if they occur.
- Internal base: volume in µL, mass in µg, money in cents with decimal (PROPOSED).
