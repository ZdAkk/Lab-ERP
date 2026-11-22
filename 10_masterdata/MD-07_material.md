# MD-07 Material (reagents and consumables)

Purpose: everything that is consumed and bought. Sample data contains "material prices and a sample stock" (BRIEF). Extends the standard ERP material (material_number, descriptions, unit, pack_size, packaging, form, primary + linked suppliers).

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| material_id, material_number | id, text unique | yes | standard ERP | |
| description | text | yes | standard ERP | |
| category | enum (base_medium, supplement, growth_factor, small_molecule, coating, enzyme, sensor/library, plate, tip, tube, other) | yes | PROPOSED | real categories OPEN: Q-M01 |
| base unit | ref MD-14 | yes | standard ERP (unit) | volume/mass/count |
| pack size + pack unit | decimal + unit | yes | standard ERP (pack_size) | |
| price per pack | money | yes | BRIEF ("material prices") | lives on MD-08 supplier article if several suppliers |
| stock concentration | decimal + unit | cond. | OPEN | needed for dilution math: Q-R02 |
| storage condition | enum | no | OPEN | |
| shelf life unopened | from lot expiry | no | OPEN | Q-M02 |
| shelf life after opening / thaw / reconstitution | duration | no | OPEN | Q-R04 |
| aliquot size | decimal + unit | no | OPEN | if thawed in aliquots, consumption granularity = aliquot: Q-R04 |
| is_consumable_counted | bool | yes | PROPOSED | include in calculation: Q-M03 |
| safety stock | decimal | no | OPEN | Q-M04 |
| hazard / handling | text | no | OPEN | not in brief |
| substance link | ref MD-10 | no | PROPOSED | if test compounds are also stock materials: Q-S01 |

Rules
- Consumption granularity: the engine consumes in base units, but if a material is used in aliquots or opened packs with limited life, waste must be computed (E-03). Whether the reference charges waste: Q-K02.

Open: Q-M01 to Q-M04, Q-R02, Q-R04, Q-K02, Q-S01
