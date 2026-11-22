# P-01 Master data import and maintenance

Trigger: Systasy sample data arrives (protocol + recipes, device list, material prices, sample stock, reference calculation). Format OPEN (Q-G02).

Steps
1. Receive files, store originals unchanged.
2. Map columns to MD entities (mapping table per file; expert checks mapping).
3. Import into staging, run validations:
   - every recipe component resolves a material; every material has unit + pack + price
   - every phase × cell type × plate format resolves a recipe (R-02)
   - units known and convertible (MD-14)
   - stock lots reference known materials; expiry present (if Q-M02 = yes)
4. Show issues in the cleanup workspace (reuse standard ERP client-seed cleanup: repair, merge duplicates, reassign).
5. Commit to master data as version 1.
6. Load the reference calculation as a fixture (input request + expected outputs) for P-12.

Output: complete master data set, list of data gaps (fed into 90_open_questions).
Roles: builder (import), domain expert (mapping check).
