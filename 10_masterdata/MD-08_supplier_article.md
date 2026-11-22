# MD-08 Supplier and supplier article

## Supplier (reuse standard ERP as is)
supplier_id, name, address, language, email, payment term, default incoterms.

## Supplier article (new link entity material x supplier)
standard ERP links materials to suppliers (primary_supplier_id, linked_supplier_ids) but price lives on the PO line. For quoting and order lists we need standing prices.

| Field | Type | Req | Status | Notes |
|---|---|---|---|---|
| supplier_article_id | id | yes | PROPOSED | |
| material_id | ref MD-07 | yes | PROPOSED | |
| supplier_id | ref | yes | PROPOSED | |
| supplier catalog number | text | no | PROPOSED | |
| pack size + unit | decimal + unit | yes | PROPOSED | may differ from material default |
| price per pack, currency | money | yes | BRIEF (material prices) | |
| price valid from / to | date | no | OPEN | Q-K04 |
| minimum order quantity | int packs | no | OPEN | Q-M04 |
| lead time | days | no | OPEN | Q-M04, drives order-by date |
| preferred | bool | yes | PROPOSED | engine picks preferred article |

Open: Q-K04, Q-M04
