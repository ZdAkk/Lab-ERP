# P-05 Media calculation

Building block 2. Engine stage 3 (spec E-02). Most likely the core of the reference calculation.

Steps
1. For each feeding task: resolve recipe (R-02), compute event volume (R-07: wells × volume per well × exchange fraction).
2. Group consecutive events of the same recipe into preparations so that every event date ≤ preparation expiry (shelf life rule Q-R04, grouping strategy Q-R05).
3. Preparation volume = sum of covered event volumes + overage/dead volume (Q-R06), rounded per rule (Q-R05).
4. For each preparation compute component amounts by spec_type (MD-06, Q-R02); base medium = remainder to volume (Q-R07).
5. For at_use components, compute amounts per event instead (Q-R03).
6. Produce recipe sheets (O2) and media plan (O1).

Output: TD-05 preparations with component lines; material demand per date.
