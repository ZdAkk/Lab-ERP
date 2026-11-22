# 90 Open questions (consolidated)

Priority: A = blocks the reference match, B = blocks a building block, C = later.
Who: SD = probably answered by the sample data, DE = domain expert (team), SW = Dr. Sven Wichert / Systasy.
Answer column to be filled during review.

## General / scope
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-G01 | Which of the 5 building blocks do we cover? (team decision, first hour) | A | team | |
| Q-G02 | Format of the sample data (Excel, CSV, PDF)? Already received? | A | SW | |
| Q-G03 | What exactly does the reference calculation contain: totals or line items? Which stages (media volumes, component amounts, order list, costs, schedule)? Where does it round? | A | SD/SW | |
| Q-G04 | One project = one cell type / one line, or several combined? | B | SW | |

## Cells
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-C01 | Is iPSC thaw/expansion before differentiation part of plan and cost, or does planning start at seeding? | A | DE/SW | |
| Q-C02 | Seeding density per well/format; source of cells (own lines, purchased progenitors)? | B | SD/DE | |
| Q-C03 | Which cell line attributes matter (donor, genotype, passage limits, data protection)? | C | SW | |
| Q-C04 | Does the cell type change the protocol, or only recipes within the same phases? | A | DE/SD | |

## Protocol
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-P01 | What is Day 0? Are phases defined by day ranges? Can phases overlap? | A | SD/DE | |
| Q-P02 | Feeding frequency and type per phase (full vs partial change, fraction)? Explicit days or a pattern? | A | SD/DE | |
| Q-P03 | Which step types exist besides feeding (coating, replating, transduction, treatment, lysis, imaging...)? Do early phases run in other vessels before replating into screening plates? | A | SD/DE | |
| Q-P04 | How flexible is each step in time (exact day vs ±n days)? Can a feeding move off a weekend? | B | DE | |
| Q-P05 | Hands-on time per step (for labour cost and capacity)? | C | DE/SW | |
| Q-P06 | Protocol versioning: do running projects keep their version? | C | SW | |

## Recipes
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-R01 | Does plate format change composition or only volume? | A | SD/DE | |
| Q-R02 | How are components specified (final conc, dilution 1:x, 50x/1x, %, mass per mL)? Stock concentrations given? Pre-diluted intermediates? | A | SD | |
| Q-R03 | Which components are added fresh at use vs into the bottle? | A | DE/SD | |
| Q-R04 | Shelf life rules: complete medium after prep; supplements after thaw/opening; aliquots; storage? | A | SD/DE | |
| Q-R05 | Prep sizes and grouping: standard bottle sizes? Prepare for N days? Prep on the day of use or before? | A | DE | |
| Q-R06 | Overage / dead volume: how much and at which level (well, plate, event, prep, reservoir)? | A | SD/DE | |
| Q-R07 | Base medium "fill to volume": are additive volumes subtracted? | A | SD | |

## Plates / layout
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-L01 | Plate formats used per phase; working volume per well (constant or per phase)? | A | SD/DE | |
| Q-L02 | Layout rules: edge wells, controls per plate (vehicle, positive, untreated), randomization? | A | DE/SW | |
| Q-L03 | Substance dimension: dose points per substance, timepoints, replicate level (wells / plates / batches)? | A | SW | |
| Q-L04 | Max plates per batch / per person per day; spare plates? | B | DE/SW | |

## Substances
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-S01 | Who supplies substances (customer / purchased)? Costed? | B | SW | |
| Q-S02 | Stock concentration, solvent (e.g. DMSO), max solvent %, dilution series steps and materials? | B | DE | |
| Q-S03 | Treatment: single dose or repeated with feedings? Several timepoints? | A | SW/DE | |

## Readouts
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-O01 | Which readouts are offered for a screen; for each: added steps, materials, devices, time to data? | A | SW | |
| Q-O02 | pathwayPROFILER: how/when are sensors introduced, materials and cost; NGS in-house or external, cost per sample? | B | SW | |
| Q-O03 | Sample level: per well, pooled, per plate? | B | SW | |

## Materials / stock
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-M01 | Material fields in the sample data (unit, pack, price, supplier, lead time, storage, shelf life)? | A | SD | |
| Q-M02 | Lot data: expiry date given? FEFO? Must a lot be valid at need date or until end of use? | B | SD/DE | |
| Q-M03 | Are consumables (plates, tips, tubes, reservoirs) part of the calculation? | A | SD | |
| Q-M04 | Order rules: pack rounding, MOQ, safety stock, lead times, split orders for short shelf life? | B | SD/SW | |
| Q-M05 | Must stock be shared with other running projects (multi-project allocation)? | C | SW | |

## Devices
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-D01 | Device list, types, capacity (incubator plate slots, hood hours), booking granularity? | B | SD | |
| Q-D02 | Which steps use which device and for how long? | B | SD/DE | |
| Q-D03 | Existing booking tool (Outlook, other)? Integration needed or mock ok? | C | SW | |

## LIMS / ELN
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-I01 | Which LIMS/ELN? What gets registered (plates, wells, samples, preps)? Import format? | C | SW | |
| Q-I02 | Sample ID / barcode conventions? | C | SW | |

## Costs / quote
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-K01 | Cost components in the reference: materials only, or also consumables, labour, device time, external, overhead, margin? Allocation key to plates? | A | SD/SW | |
| Q-K02 | Material cost on exact use or on opened packs/aliquots (waste charged)? | A | SD/SW | |
| Q-K03 | What is a "batch" in "cost per plate, batch and project"? | A | SW | |
| Q-K04 | Currency, VAT, discounts, price validity? | C | SW | |
| Q-K05 | What does the customer quote show (per plate, per compound, total)? | B | SW | |

## Calendar / staff
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-W01 | Working days; is weekend work allowed for which steps? | B | DE/SW | |
| Q-W02 | Model staff capacity, or not? | C | SW | |

## Planning
| ID | Question | Prio | Who | Answer |
|---|---|---|---|---|
| Q-PL01 | "Desired date" = start, readout, or result delivery? Time from readout to delivery? | A | SW | |
| Q-PL02 | Which conflicts matter most; hard vs soft constraints? | B | SW | |
| Q-PL03 | Replanning during execution in scope? | C | SW | |

## Top 10 to ask Sven Wichert first
Q-G03, Q-K03, Q-PL01, Q-K01, Q-K02, Q-L03, Q-O01, Q-C01, Q-G04, Q-S03
