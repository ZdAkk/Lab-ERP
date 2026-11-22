# R-07 Plate → plate format (volume scaling)

- Plate n : 1 Plate format.
- Plate format supplies working volume per well (possibly per phase: Q-L01) and usable wells (Q-L02).

Volume per feeding event (structure PROPOSED)
- event_volume = wells_fed × volume_per_well × exchange_fraction (Q-P02)
- then overage / dead volume (Q-R06) applied in E-02, at a level still OPEN (per plate, per event, per preparation).

Open: Q-L01, Q-L02, Q-P02, Q-R06
