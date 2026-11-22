# R-03 Recipe BOM: recipe → component → material

- Recipe 1 : n Component; Component n : 1 Material.
- Base medium is a component with spec_type fill_to_volume (PROPOSED, Q-R07).
- A component may itself be a prepared intermediate (e.g. a pre-diluted stock), making the BOM multi-level: OPEN whether this exists (Q-R02). Model allows it: Component → Material where Material has its own recipe (PROPOSED).

Rules
- Each component carries add_timing (at_preparation / at_use) (Q-R03).
- Volume of all additives is subtracted from base medium volume (PROPOSED; confirm convention against reference).

Open: Q-R02, Q-R03, Q-R07
