# DSS150P Lab 01: Data Profiling and Environment Setup
**Name:** Sophia Aguirre  
**Student Number:** 2024109563

## Purpose of the Laboratory
The purpose of this laboratory is to establish a reproducible local data engineering environment using Python, Git, and Docker. It involves profiling various data formats (CSV, JSON, Parquet, REST API, and PostgreSQL) to uncover data quality issues, documenting these findings, and defining a formal data contract and SQL schema for future automated ingestion pipelines.

## Software Requirements
* Git
* Python 3.10 or higher
* Docker Desktop
* Visual Studio Code (with Python and Docker extensions recommended)

## Exact Steps to Reproduce the Environment
1. Clone the repository to your local machine using Git.
2. Open the cloned folder in VS Code.
3. Open a new terminal and create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
   * Windows: `.\.venv\Scripts\activate`
   * Mac/Linux: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Database Management Commands
* **Start PostgreSQL:** `docker compose up -d`
* **Stop PostgreSQL:** `docker compose down`

## How to Run Each Python Script
* **Verify Environment:** `python src/verify_environment.py`
* **Profile Sources:** `python src/profile_sources.py`
* **Inspect API:** `python src/inspect_api.py`

## Description of Each Source
* **customers.csv:** A flat file containing customer demographic data. Profiling showed it contains duplicate rows and missing values in `email` and `city`.
* **orders.json:** Transactional data containing order totals and nested JSON objects for shipping details.
* **products.parquet:** Columnar storage file containing product inventory and pricing data. High structural integrity with zero missing values.
* **REST API:** Mock JSON placeholder API endpoint (`/posts`) returning list-based mock data.
* **PostgreSQL:** A relational database table (`support_tickets`) containing customer support tickets and status timestamps.

## Known Limitations and Unresolved Questions
* The `email` validation rules in the data contract need to be verified with the business owners to ensure we do not reject valid legacy customer records.
* The expected update pattern (batch vs. incremental) is currently an assumption and requires confirmation from the source owner.

## AI Usage
* **Tool Used:** Gemini (Google AI)
* **Assisted Tasks:**
  * **Troubleshooting Terminal Errors:** Resolved the Python `TypeError: unhashable type: 'dict'` in `profile_sources.py` when profiling nested JSON, resolved the PowerShell `<` redirection error using `Get-Content`, and resolved the PostgreSQL container role/database login error (`dss150p` user).
  * **Terminal Navigation:** Provided instructions to exit the terminal pager (`less` viewer) using `q` when running SQL queries.
  * **Code & Schema Generation:** Assisted in drafting `sql/01_create_schema.sql` with appropriate data types/constraints, `docs/data_contract.yaml`, `docs/reflection.md`, and formatting terminal output into clean Markdown tables.
  * **Environment Execution Guidance:** Guided step-by-step commands for running Python scripts, Docker container queries, Git commands, and saving evidence files (`customer_schema_evidence.txt`).
* **Verification & Personal Verification:**
  * Independently executed all terminal commands, SQL scripts, and Python profiling scripts in the local environment.
  * Verified that database tables, schemas, and evidence text files were generated correctly.
  * Validated that all generated documentation (`docs/source_profile.md`, `docs/data_contract.yaml`, `docs/reflection.md`, `README.md`) accurately matched the live execution results before committing and pushing to Git.