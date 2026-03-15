# job-data-engineering-pipeline
Web Scraping → ETL Pipeline → SQLite Data Warehouse → SQL Analysis → Power BI Dashboard
Job Data Engineering Pipeline
Overview

This project demonstrates an end-to-end Data Engineering pipeline for collecting, transforming, and analyzing job postings.
All data is ingested via an API (no web scraping), cleaned, and loaded into a SQLite Data Warehouse following a star schema.

The pipeline shows practical skills in:

API-based data ingestion

Data cleaning & ETL with Python and Pandas

Data warehouse modeling

SQL analysis

Power BI visualization

CI/CD automation with GitHub Actions

Folder & File Structure
job-data-engineering-pipeline
│
├── .github/workflows        # CI/CD automation for scraping, ETL, and database updates
├── data/raw                 # Raw API data before cleaning
│   └── jobs.csv
├── data/processed           # Cleaned data ready for database loading
├── scraper                  # Scripts to fetch job listings from API
│   └── scraper.py
├── pipeline                 # ETL and loader scripts
│   ├── etl.py
│   └── loader.py
├── database                 # Data warehouse schema (star schema)
│   └── schema.sql
├── analysis                 # SQL queries for insights
│   └── queries.sql
├── dashboard                # Power BI dashboard files
│   └── jobs_dashboard.pbix
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies

Description of each folder:

.github/workflows – Automates the pipeline using GitHub Actions for scheduled and manual runs.

data/raw – Stores the original job data retrieved from the API.

data/processed – Contains cleaned and transformed data ready to load into the data warehouse.

scraper – Python scripts responsible for calling the job API and saving raw data.

pipeline – ETL scripts: etl.py cleans & transforms data, loader.py loads data into the warehouse.

database – SQL schema defining fact and dimension tables, implementing a star schema.

analysis – SQL queries to generate insights from the data warehouse.

dashboard – Power BI dashboards built from the data warehouse.

requirements.txt – Python dependencies.

Data Warehouse Design (Star Schema)

Your data warehouse uses a star schema:

Fact Table: fact_jobs – central table storing job postings

Dimension Tables: dim_company (company info), dim_tags (job skill tags)

Fact Table: fact_jobs

Stores events (job postings) and references dimensions. Includes:

fact_id – primary key

job_id – unique job identifier

company_id – links to dim_company

position – job title

min_salary / max_salary / avg_salary

posted_date – job posting date

url – job link

loaded_at – timestamp for when the record was added

Dimension Tables

dim_company – stores descriptive company information:

company_id – primary key

company_name – unique company name

dim_tags – stores job skill tags:

tag_id – primary key

tag_name – unique tag name

Diagram (Star Schema)

                    +-------------------+
                    |    dim_company    |
                    |-------------------|
                    | company_id (PK)   |
                    | company_name      |
                    +---------+---------+
                              |
                              |
                              |
                      +-------+-------+
                      |    fact_jobs   |
                      |---------------|
                      | fact_id (PK)  |
                      | job_id        |
                      | company_id FK |
                      | position      |
                      | min_salary    |
                      | max_salary    |
                      | avg_salary    |
                      | posted_date   |
                      | url           |
                      | loaded_at     |
                      +-------+-------+
                              |
                              |
                              |
                    +---------+---------+
                    |      dim_tags     |
                    |-------------------|
                    | tag_id (PK)       |
                    | tag_name          |
                    +-------------------+
Full Pipeline Process
        Job API
           │
           ▼
    scraper/scraper.py
   (API → data/raw/jobs.csv)
           │
           ▼
      pipeline/etl.py
   (Clean & transform data)
           │
           ▼
    pipeline/loader.py
   (Load into SQLite DW)
           │
           ▼
    SQLite Data Warehouse
   +------------------------+
   | fact_jobs (central)    |
   | dim_company            |
   | dim_tags               |
   +------------------------+
           │
           ▼
     analysis/queries.sql
   (SQL analysis & insights)
           │
           ▼
  dashboard/jobs_dashboard.pbix
   (Power BI visualizations)
           │
           ▼
.github/workflows/pipeline.yml
  (Automates scraper, ETL, loader, and pushes updated data)

Description of each step:

Job API – Source of job postings.

scraper/scraper.py – Calls the API and saves raw data as CSV.

pipeline/etl.py – Cleans, transforms, and prepares data for loading.

pipeline/loader.py – Loads processed data into the star schema in SQLite.

SQLite Data Warehouse – Stores the central fact table and dimensions.

analysis/queries.sql – Executes SQL queries to analyze job trends, companies, and salaries.

dashboard/jobs_dashboard.pbix – Power BI dashboards for visualization.

.github/workflows/pipeline.yml – Automates all steps monthly or manually via GitHub Actions.

SQL Analysis Examples

Count of jobs per company

Average salary per position

Job posting trends over time

CI/CD Automation

GitHub Actions runs the pipeline monthly or manually.

Automatically updates data/raw, data/processed, and the SQLite warehouse.

Commits and pushes updated data back to the repository.

Future Improvements

Add more dimensions (location, job type, experience level)

Deploy warehouse to a cloud database

Live dashboards with real-time updates

Integration with additional job APIs




Author

Apurva – Data Engineering Student

Skills demonstrated: Python ETL pipelines, API data ingestion, data warehouse modeling, SQL analysis, Power BI dashboards, CI/CD automation.
