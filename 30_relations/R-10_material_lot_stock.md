# R-10 Material → lot → movement / reservation

- Material 1 : n Lot; Lot 1 : n Movement; Lot 1 : n Reservation (standard ERP pattern).
- Reservation can point to a lot or to an incoming PO item (standard ERP pattern) and now carries a need date.

Rules
- available(lot, date) = on_hand − reserved, only if expiry ≥ date (PROPOSED; exact expiry check OPEN Q-M02).
- Reservation allocation order FEFO/FIFO (MD-17, Q-M02).

Open: Q-M02, Q-M05
