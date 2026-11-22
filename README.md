# Lab screen planning ERP — blueprint

Blueprint for the Systasy Bioscience challenge, LMU Startup in 2 Days, team 1.
Version 0.1, 21.11.2026. Draft for domain expert review.

Open `index.html` in a browser for the visual overview: the calculation pipeline,
the data model spine, a linked map of all 71 documents, and the questions to ask
Systasy first. It is one self-contained file, no build step and no dependencies.

## What this is

From a few parameters (cell types, plates, substances, replicates, readouts,
desired date) plan a multi-month drug screen on stem-cell-derived neurons:
media recipes per phase and day, a project plan with conflict warnings, an order
list checked against stock, and cost per plate, batch and project.

Success is measured by matching Systasy's reference calculation.

## Conventions

Every field and rule carries a status:

- BRIEF: stated in the problem brief or on Systasy's own website and job ad. Given.
- PROPOSED: our structure, needed so the engine can work. Confirm or reject.
- OPEN: unknown, not guessed. Points at a question ID in `90_open_questions.md`.

No domain values (volumes, concentrations, shelf lives, day counts, prices) are
invented anywhere. Where a value is needed, the field exists and is left empty.

## Layout

| Path | Contents |
|---|---|
| `00_INDEX.md` … `08_mvp_plan.md` | Context, glossary, input form, outputs, architecture, plan |
| `10_masterdata/` | MD-01 to MD-17, the Stammdaten |
| `20_transactions/` | TD-01 to TD-12, the Bewegungsdaten |
| `30_relations/` | R-00 to R-12, including the ER diagram |
| `40_processes/` | P-01 to P-12, the workflows |
| `50_engine/` | E-01 to E-07, the calculation specs |
| `90_open_questions.md` | All open questions, grouped, prioritised, with owners |

## Review order

1. `90_open_questions.md` first. Mark each: answer, "in the sample data", or "not relevant".
2. Master data: is an entity missing, is a PROPOSED field wrong?
3. Processes P-04 to P-06 (schedule, media, materials): is the order of steps realistic?
