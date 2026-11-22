# Blueprint: Lab Screen Planning ERP (Team 1, Systasy challenge)

Version 0.1, 21.11.2026. Draft for domain expert review.

## Goal
From a few parameters (cell types, plates, substances, replicates, readouts, desired date) plan a multi-month drug screen on stem-cell-derived neurons: media recipes per phase and day, project plan with conflict warnings, order list checked against stock, cost per plate, batch and project. Success = match Systasy's reference calculation.

## Conventions used in every document
Every field, rule and value carries a status:

- BRIEF: stated in the LMU problem brief or on Systasy's own website / job ad. Treat as given.
- PROPOSED: structural proposal by us (needed so the engine can work). Domain expert must confirm or reject.
- OPEN: unknown. Not guessed. Linked to a question ID (Q-xx) in `90_open_questions.md`.

No domain values (volumes, concentrations, shelf lives, day counts, prices) are invented anywhere. Where a value is needed, the field exists and the value is OPEN, to be filled from the Systasy sample data or the domain expert.

## Document map
- `01_context.md` sources, Systasy, problem, success criterion
- `02_glossary.md` terms (bio + ERP), with ambiguous terms flagged
- `03_input_form.md` screen request parameters
- `04_outputs.md` what the system produces
- `05_standard_erp_blocks.md` what is ordinary ERP machinery and what is genuinely new
- `06_status_models.md` state machines
- `07_architecture.md` engine + ERP shell, determinism, trace
- `08_mvp_plan.md` build plan until the pitch on 27.11.

Master data (Stammdaten), folder `10_masterdata/`
- MD-01 cell line, MD-02 cell type, MD-03 protocol, MD-04 protocol phase, MD-05 protocol step, MD-06 media recipe (+components), MD-07 material, MD-08 supplier + supplier article, MD-09 plate format, MD-10 substance, MD-11 readout, MD-12 device, MD-13 customer, MD-14 units, MD-15 cost rates, MD-16 work calendar + staff, MD-17 calculation settings

Transactional data (Bewegungsdaten), folder `20_transactions/`
- TD-01 screen project, TD-02 screen batch, TD-03 plate + well, TD-04 task, TD-05 media preparation, TD-06 stock lot + movement, TD-07 reservation, TD-08 order list + purchase order, TD-09 device booking, TD-10 cost calculation + quote, TD-11 LIMS sample, TD-12 audit + calculation trace

Relations, folder `30_relations/`: R-00 ER overview, R-01 to R-12

Processes, folder `40_processes/`: P-01 to P-12

Calculation engine, folder `50_engine/`: E-01 to E-07

Open questions: `90_open_questions.md` (single consolidated list, grouped, with priority and who answers)

## How to review (for the domain expert)
1. Read `90_open_questions.md` first. Mark each question: answer / "in sample data" / "not relevant".
2. Then skim master data: is an entity missing? Is a PROPOSED field wrong?
3. Then processes P-04 to P-06 (schedule, media, materials): is the order of steps realistic?
