# R-08 Step → resources

Step 1 : n Resource line. A resource line is one of:
- material (material id, quantity, unit, basis)
- device (device type, duration or capacity, basis)
- labour (hands-on time, basis)
- external service (service, quantity basis)

Basis enum (PROPOSED): per_well, per_plate, per_batch, per_project, per_event, per_preparation.

Rules
- Feeding steps get their media demand from the recipe (R-02), not from resource lines.
- Consumables used in feeding (tips, reservoirs) are resource lines if counted (Q-M03).

Open: Q-M03, Q-D02, Q-P05
