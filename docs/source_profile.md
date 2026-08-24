# Source Data Profile Observations

## 1. customers.csv
* **Observation 1 (Duplicates & Primary Key Risk):** The dataset contains **2 fully duplicated rows** (250 total rows, but only 247 distinct `customer_id` values). A downstream pipeline must execute deduplication (e.g., `df.drop_duplicates()`) before database ingestion to avoid Primary Key constraint violations.
* **Observation 2 (Data Quality & Nullability):** There are missing values in text attributes (**3 missing `email` values** and **2 missing `city` values**). The pipeline needs imputation logic (e.g., filling with `"Unknown"`) or strict validation rules depending on business requirements.

## 2. orders.json
* **Observation 1 (Nested JSON Structure):** The `shipping` column contains nested dictionary objects (e.g., `{'region': 'Region VII', 'method': 'Standard'}`). The ingestion process must flat/normalize this struct using `pd.json_normalize()` to extract `region` and `method` into relational columns.
* **Observation 2 (Type Ambiguity & Time Ranges):** `order_timestamp` is parsed as a generic string/object rather than a native datetime type. The pipeline must explicitly cast it to a timestamp (ranging from `2026-01-02 03:00:00` to `2026-06-30 07:38:00`). Additionally, `status` has 6 distinct values and `shipping_fee` has 5, making them strong candidates for categorical validation.

## 3. products.parquet
* **Observation 1 (Schema Enforcement & File Efficiency):** Despite holding 200 rows with 7 columns, the Parquet file size is only **14.31 KB** (compared to `orders.json` at 79.53 KB). Strongly typed columns like `stock_quantity` (int32) and `weight_kg` (float64) retain their exact types without manual type casting during import.
* **Observation 2 (Dimensional Modeling & Outliers):** High cardinalities exist for `product_id` and `product_name` (200 distinct), while `category` and `brand` contain only **6 distinct values each**, making them ideal dimension dimensions. Price ranges are wide (Min = 392.85, Max = 84,796.84), requiring validation rules to check for price anomalies.

## 4. PostgreSQL: support_tickets
* **Table Name:** `support_tickets`
* **Row Count:** 250

**Columns, Data Types, & Nullable:**
* `ticket_id` (integer, NOT NULL)
* `customer_id` (character varying, NOT NULL)
* `category` (character varying, NOT NULL)
* `priority` (character varying, NOT NULL)
* `assigned_agent` (character varying, NULL)
* `opened_at` (timestamp without time zone, NOT NULL)
* `resolved_at` (timestamp without time zone, NULL)
* `status` (character varying, NOT NULL)

**Sample Rows:**
| ticket_id | customer_id | category | priority | assigned_agent | opened_at | resolved_at | status |
|---|---|---|---|---|---|---|---|
| 1 | C0246 | Technical | High | J. Reyes | 2026-06-19 04:00:00 | 2026-06-21 13:00:00 | Resolved |
| 2 | C0130 | Product | Medium | J. Reyes | 2026-05-26 07:00:00 | 2026-05-26 23:00:00 | Closed |
| 3 | C0094 | Delivery | Medium | J. Reyes | 2026-03-28 09:00:00 | 2026-03-31 17:00:00 | Closed |
| 4 | C0057 | Technical | High | L. Tan | 2026-04-25 19:00:00 | | In Progress |
| 5 | C0120 | Delivery | High | R. Cruz | 2026-01-20 02:00:00 | 2026-01-22 21:00:00 | Resolved |