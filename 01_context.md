# 01 Context and sources

## Sources used
1. LMU Startup in 2 Days, Team 1 sheet (project file `Team_01_Lab_Automation_and_Cell_Culture_Screens-2.pdf`)
2. systasy.de: company, technology (pathwayPROFILER, targetFinder), human disease models, pathwayPROFILER screening page, news, careers
3. Systasy job ad "Laboratory Technician Stem Cell Culture" (Oct 2026, PDF on systasy.de/careers)
4. Prior experience building a production ERP for purchasing, warehousing and sales, used to separate standard ERP machinery from what has to be built new

## Systasy facts relevant for the model (BRIEF)
- Munich biotech, founded 2012, CEO Dr. Sven Wichert (problem giver). Lab in Planegg-Martinsried (new facility May 2025).
- Core: barcoded cell-based assays. pathwayPROFILER = synthetic sensor constructs reporting >30 signaling pathways, readout by next-generation sequencing (NGS). Stated as suitable for neurons, iPSC-derived models, primary cells, and for 96- and 384-well formats.
- targetFinder = pooled RNAi or CRISPR screens combined with activity sensors.
- Human disease models: patient-derived iPSC models, 2D and 3D. Differentiated into excitatory or inhibitory neurons, sensory neurons, oligodendrocytes. Donor data includes genetic, MRI and clinical data.
- Job ad (stem cell technician) daily work: maintain, expand and cryopreserve iPSCs; run neuronal differentiation; support assays and screens; monitor cell health and differentiation quality; prepare and manage media, reagents, samples incl. stock keeping; document in an ELN; follow SOPs. No LIMS product, devices, plate formats or automation named.

## Problem (BRIEF, from the team sheet)
- A screen on stem-cell-based neurons runs weeks to months. Dozens of media recipes per phase, plate format and cell type.
- Planning, device booking, ordering, LIMS entries and costing run separately and by hand. A calculation error or missing reagent can cost a whole batch. Each customer quote takes hours.
- Five building blocks suggested by Systasy:
  1. Input form (cell types, plates and format, substances, replicates, readouts, desired date)
  2. Media recipes per phase and day incl. volumes, additives, shelf life
  3. Project plan with daily tasks, backward planning from delivery date, conflict warnings
  4. Device booking in a calendar, samples in the LIMS, order list checked against stock
  5. Costs per plate, batch and project as basis for quotes
- Sample data promised (simplified/fictional, non-critical): a multi-week differentiation and screening protocol with media recipes; a device list; material prices; a sample stock; a reference calculation for one sample screen.
- Success: match with the reference calculation. Suggested disciplines: software development, operations research, business administration.
- Which building blocks to cover is not prescribed.

## Our framing
This is an ERP for a cell culture service lab where the "bill of materials" is a time-dependent protocol. The standard ERP already solves suppliers, materials, purchase orders, batch-aware stock, reservations, audit and data cleanup. New are: protocol and recipe modeling, the calculation engine, scheduling with conflicts, devices, and project costing.

## What we deliberately do not know yet
See `90_open_questions.md`. The most important unknown is the exact content and output shape of the reference calculation (Q-G03), because it defines what "correct" means.
