# 02 Glossary

Terms flagged AMBIGUOUS must be pinned down with the domain expert before coding, because they change the data model.

| Term | Meaning in this blueprint | Status |
|---|---|---|
| iPSC | induced pluripotent stem cell; starting material, expanded and cryopreserved | BRIEF |
| Cell line | a specific iPSC line (e.g. from one donor/patient) | BRIEF (concept), fields OPEN |
| Cell type | target cell after differentiation (e.g. excitatory neuron) | BRIEF |
| Differentiation | multi-week protocol turning iPSCs into the cell type, run in phases with changing media | BRIEF |
| Protocol | template describing phases, steps, recipes, timing | PROPOSED |
| Phase | time segment of a protocol with one media regime (recipe) | BRIEF ("recipes per phase") |
| Day (protocol day) | day offset within the protocol, relative to a Day 0 | PROPOSED, Day 0 definition OPEN (Q-P01) |
| Step / task | an action on a given day (feeding, coating, seeding, treatment, readout...) | PROPOSED |
| Medium change / feeding | replacing (all or part of) the medium in wells | OPEN details (Q-P02) |
| Media recipe | composition of a complete medium: base medium + additives with concentrations | BRIEF |
| Component / additive | one ingredient of a recipe (supplement, growth factor, small molecule...) | BRIEF ("additives") |
| Shelf life | how long something stays usable: prepared medium, opened/thawed supplement, stock lot | BRIEF (concept), rules OPEN (Q-R04) |
| Plate format | 96-well, 384-well etc.; defines wells and volumes | BRIEF (96/384 on website), volumes OPEN |
| Well | one compartment of a plate | BRIEF |
| Substance | test compound to be screened | BRIEF |
| Replicate | repeated measurement of the same condition | BRIEF, level OPEN (Q-L03) |
| Condition | one combination of substance + concentration (+ timepoint?) | PROPOSED |
| Control | vehicle/positive/negative wells | OPEN (Q-L02) |
| Readout | the measurement at the end (e.g. pathwayPROFILER via NGS) | BRIEF |
| Batch | AMBIGUOUS. In the brief "cost per plate, batch and project". Could mean a group of plates run together (same seeding day / same differentiation run). Not the same as a stock lot. | OPEN (Q-K03) |
| Lot (Charge) | a received delivery of a material with lot number and expiry. In standard ERP this is called "batch"; here we call it lot to avoid collision with screen batch. | PROPOSED naming |
| Media preparation | one physical preparation of a recipe (e.g. one bottle) with prep date and expiry | PROPOSED |
| Dead volume / overage | extra volume beyond what lands in wells (pipetting loss, reservoir) | OPEN (Q-R06) |
| Order list | net material requirement after stock, rounded to purchasable packs | BRIEF |
| LIMS / ELN | lab information management system / electronic lab notebook. Job ad mentions an ELN only. | BRIEF (ELN), LIMS product OPEN (Q-I01) |
| Device | bookable lab equipment (incubator, hood, liquid handler, imager...) | BRIEF (device list in sample data) |
| Reference calculation | Systasy's own worked calculation for one sample screen; our acceptance test | BRIEF |
| Snapshot | copy of master data values frozen into a transaction (pattern from standard ERP) | PROPOSED |
