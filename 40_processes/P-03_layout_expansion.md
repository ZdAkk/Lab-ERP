# P-03 Layout expansion (parameters → plates, wells, batches)

Engine stage 1 (E-01).

Steps
1. Build conditions from substances × concentrations (× timepoints, OPEN Q-S03).
2. Add replicates at the configured level (Q-L03).
3. Add control wells (Q-L02).
4. Fit into plates using usable wells (Q-L02), add spares (Q-L04).
5. Group plates into batches (Q-K03, Q-L04).
6. Optional: generate explicit well map (for LIMS export / plate print).

Output: counts per plate format, plate list, batch list, optional well map. Trace nodes for every count.
