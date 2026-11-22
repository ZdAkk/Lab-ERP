# R-11 Task → preparation → lots consumed

- Feeding task n : 1 Preparation (a preparation covers several feedings until expiry).
- Preparation 1 : n Component line; Component line n : 1 Lot at execution (planning: reservation only).

Rules
- Preparation date ≤ first covered task date; expiry ≥ last covered task date.
- at_use components (Q-R03) link directly from task to material, not via preparation.

Open: Q-R03, Q-R04, Q-R05
