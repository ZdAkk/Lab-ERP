# R-06 Project → batch → plate → well

- Project 1 : n Batch (meaning OPEN: Q-K03), Batch 1 : n Plate, Plate 1 : n Well, Well n : 0..1 Condition.

Derivation (structure PROPOSED, all parameters OPEN)
- wells_needed = conditions × replicates_per_condition + control wells (Q-L02, Q-L03)
- plates = ceil(wells_needed / usable_wells_per_plate) + spare plates (Q-L04) OR entered directly (input F07)
- batches = f(plates, max plates per batch) (Q-L04, Q-K03)

Rules
- If replicates are across plates or batches instead of wells, the formula changes; decided by Q-L03.

Open: Q-K03, Q-L02, Q-L03, Q-L04
