# E-02 Media calculation spec

Only standard dilution arithmetic is assumed. Conventions (which overage, where rounding) are parameters (MD-17), all OPEN until the reference is seen.

## 1 Event volume (per feeding task)
V_event = n_wells_fed × v_well(phase, plate format) × f_exchange(step)
- n_wells_fed: all wells or only used wells? (Q-L02)
- v_well: Q-L01; f_exchange: Q-P02

## 2 Preparation grouping
Events of the same recipe ordered by date. Open a preparation at the first uncovered event; add following events while event_date ≤ prep_date + shelf_life (Q-R04). Alternative strategies selectable (one prep per event, fixed weekly): Q-R05.
- prep_date = first event date, or earlier day (Q-R05)

## 3 Preparation volume
V_prep = Σ V_event × (1 + overage_pct) + dead_volume (level and values: Q-R06)
then rounding to standard sizes / step (Q-R05)

## 4 Component amounts by spec_type
- final_concentration: amount_vol = V_prep × c_final / c_stock (units converted via MD-14)
- dilution_factor (e.g. 1:100): amount_vol = V_prep / factor
- ratio "x" (e.g. 50x to 1x): amount_vol = V_prep × target / stock
- percent_v_v: amount_vol = V_prep × pct / 100
- amount_per_volume (e.g. mass per mL): amount = V_prep × value
- fill_to_volume (base medium): V_base = V_prep − Σ additive volumes (convention: Q-R07)
Which spec types actually appear and whether additive volumes are subtracted: Q-R02, Q-R07.

## 5 At-use components
Computed per event on V_event instead of V_prep (Q-R03).

## 6 Expiry
expiry(prep) = prep_date + shelf_life(recipe), possibly min with component open-life (Q-R04).

## Outputs
O1 media plan, O2 recipe sheets, demand lines (material, amount, need date = prep_date or event date).
