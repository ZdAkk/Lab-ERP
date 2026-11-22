# 07 Architecture (PROPOSED)

## Two layers
1. Calculation engine: a pure, deterministic function.
   `calculate(request, masterDataSnapshot, stockSnapshot, settings) → { schedule, mediaPlan, preparations, materialNeeds, orderList, bookings, costs, conflicts, trace }`
   No database access, no clock (today's date is an input). Same inputs give the same outputs. This makes "match the reference calculation" a unit test.
2. ERP shell: master data maintenance, import, projects, stock, purchasing, quotes, audit. Based on the standard ERP foundation (same stack, same patterns: snapshots, status + lock, movement ledger, reservations, audit).

## Engine pipeline (details in E-01)
request → expand layout (plates, wells, batches) → build schedule (protocol steps placed on calendar, backward from desired date) → media demand per feeding event → group demand into preparations (shelf life) → explode preparations into components (recipe BOM) → add step materials and consumables → time-phased material need → net against stock lots (expiry aware) and incoming → order list (pack rounding, lead time → order-by date) → device demand → conflicts → costs.

## Determinism rules
- Decimal arithmetic, never floats, for all quantities and money.
- Rounding only at configured points (MD-17), each rounding written to the trace. Where the reference rounds is OPEN (Q-G03); rounding points must therefore be configurable, not hard-coded.
- Units normalized internally (MD-14), converted only for display.
- Stable ordering everywhere (sort keys defined), so lists compare 1:1 with the reference.

## Trace
Every computed number is a trace node: id, label, value, unit, formula text, input node ids, rounding applied. O10 (reference comparison) and debugging both read the trace. When our total differs from the reference, the trace shows which line diverges.

## Data versioning
- Master data changes create new versions (or at least updated_at + snapshot on use).
- A project stores the calculation run id it was quoted on.

## Integrations (all OPEN, mock first)
- LIMS / ELN export (Q-I01), device calendar (Q-D03), supplier ordering by email (standard ERP already uses mailto flows).
