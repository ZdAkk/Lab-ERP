# R-00 ER overview

Mermaid diagram (paste into any Mermaid renderer). Cardinalities are PROPOSED; open ones are marked in the relation docs.

```mermaid
erDiagram
  PROTOCOL ||--|{ PHASE : "has (R-01)"
  PHASE ||--|{ STEP : "has (R-01)"
  CELL_TYPE }o--o{ PROTOCOL : "uses"
  PHASE ||--o{ RECIPE_RULE : "resolves (R-02)"
  CELL_TYPE ||--o{ RECIPE_RULE : ""
  PLATE_FORMAT ||--o{ RECIPE_RULE : ""
  RECIPE_RULE }o--|| RECIPE : ""
  RECIPE ||--|{ RECIPE_COMPONENT : "BOM (R-03)"
  RECIPE_COMPONENT }o--|| MATERIAL : ""
  MATERIAL ||--o{ SUPPLIER_ARTICLE : "R-04"
  SUPPLIER ||--o{ SUPPLIER_ARTICLE : ""
  STEP ||--o{ STEP_RESOURCE : "R-08"
  STEP_RESOURCE }o--o| MATERIAL : ""
  STEP_RESOURCE }o--o| DEVICE_TYPE : ""
  READOUT ||--o{ STEP : "adds steps (R-09)"
  CUSTOMER ||--o{ PROJECT : ""
  PROJECT }o--|| PROTOCOL : "R-05"
  PROJECT }o--o{ CELL_LINE : "R-05"
  PROJECT }o--o{ READOUT : "R-05"
  PROJECT ||--|{ CONDITION : "R-05"
  CONDITION }o--|| SUBSTANCE : ""
  PROJECT ||--|{ BATCH : "R-06"
  BATCH ||--|{ PLATE : "R-06"
  PLATE }o--|| PLATE_FORMAT : "R-07"
  PLATE ||--o{ WELL : "R-06"
  WELL }o--o| CONDITION : ""
  PROJECT ||--o{ TASK : ""
  TASK }o--|| STEP : "instance of"
  TASK }o--o| PREPARATION : "R-11"
  PREPARATION }o--|| RECIPE : ""
  MATERIAL ||--o{ LOT : "R-10"
  LOT ||--o{ MOVEMENT : "R-10"
  LOT ||--o{ RESERVATION : "R-10"
  RESERVATION }o--|| PROJECT : ""
  PROJECT ||--o{ ORDER_LINE : ""
  ORDER_LINE }o--o| PO_ITEM : ""
  TASK ||--o{ DEVICE_BOOKING : ""
  DEVICE_BOOKING }o--|| DEVICE : ""
  PROJECT ||--o{ COST_LINE : "R-12"
  PROJECT ||--o{ QUOTE : ""
```

## Relation docs
- R-01 Protocol → phase → step
- R-02 Recipe resolution (phase × cell type × plate format → recipe)
- R-03 Recipe BOM (recipe → component → material)
- R-04 Material ↔ supplier (supplier article)
- R-05 Project → protocol, cell lines/types, readouts, conditions
- R-06 Project → batch → plate → well
- R-07 Plate → plate format (volume scaling)
- R-08 Step → resources (materials, devices, labour)
- R-09 Readout → added steps and resources
- R-10 Material → lot → movement / reservation
- R-11 Task → preparation → lots consumed
- R-12 Project → cost lines → sources
