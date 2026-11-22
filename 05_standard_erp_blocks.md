# 05 Standard ERP blocks and what is genuinely new

Roughly half of this system is ordinary ERP machinery that any purchasing and warehouse system has. The other half does not exist in any ERP, because it depends on time and biology. Separating the two decides where the two days of build time go.

## Already solved by standard ERP patterns

| Block | What it covers |
|---|---|
| Supplier and material master | Numbers, descriptions, units, pack sizes, supplier links |
| Purchasing | Purchase order, confirmation, lock, shipment, goods receipt |
| Warehouse | Physical stock per lot, incoming stock, manual adjustments, movement ledger |
| Reservations | Reserve from stock on hand, from incoming orders, or a mix |
| Customer and quoting | Customer master, offer document, validity date, payment terms |
| Audit | Who changed what and when, before and after |
| Import and cleanup | Repair imported records, merge duplicates, reassign links |
| Snapshots | Freeze master data values into a document so later edits cannot rewrite history |

These need adapting, not inventing. The main additions are expiry dates on lots, an opened date, and a need date on reservations so they become time phased.

## Genuinely new, built from scratch

1. Protocol, phase and step model: a bill of materials that unfolds over weeks
2. Recipes with concentrations, and the dilution arithmetic behind them
3. Units with volume, mass and concentration conversion
4. Plate formats, plates and well layout
5. The calculation engine with a full trace
6. Backward scheduling against a calendar, with conflict detection
7. Devices with two capacity models, time and space
8. Shelf life on preparations and lots
9. Project cost roll-up to plate, batch and project
10. LIMS export

## Why this matters for the two days

Everything in the first table is plumbing that can be assembled quickly. Everything in the second table is where the reference calculation lives, so that is where the build time goes.
