# job-data-engineering-pipeline

# 🛠️ Job Data Engineering Pipeline

**End-to-end pipeline** for collecting, transforming, and analyzing job postings via an **API → ETL → SQLite → SQL → Power BI** workflow.

---

## 🚀 What It Does

* Fetches job postings from an API
* Cleans and transforms data with **Python & Pandas**
* Loads data into a **SQLite Data Warehouse** (star schema)
* Analyzes with **SQL**
* Visualizes trends with **Power BI**
* Automated with **GitHub Actions**

---

## 🗂️ Project Structure

```
job-data-engineering-pipeline/
│
├─ .github/workflows   # CI/CD automation
├─ data/raw            # Raw API data
├─ data/processed      # Cleaned & ready-to-load data
├─ scraper/            # API fetching scripts
├─ pipeline/           # ETL & loader scripts
├─ database/           # Star schema SQL
├─ analysis/           # SQL queries for insights
├─ dashboard/          # Power BI dashboards
├─ README.md
└─ requirements.txt
```

---

## 💡 Data Warehouse (Star Schema)

**Fact Table: `fact_jobs`** – central job postings

* `fact_id` | `job_id` | `company_id` | `position` | `min_salary` | `max_salary` | `avg_salary` | `posted_date` | `url` | `loaded_at`

**Dimension Tables:**

* `dim_company` → `company_id`, `company_name`
* `dim_tags` → `tag_id`, `tag_name`

```
dim_company
    |
    v
fact_jobs
    |
    v
dim_tags
```

---

## 🔄 Pipeline Flow

```
Job API
  ↓
scraper/scraper.py → data/raw/jobs.csv
  ↓
pipeline/etl.py → cleaned & transformed
  ↓
pipeline/loader.py → SQLite DW
  ↓
analysis/queries.sql → insights
  ↓
dashboard/jobs_dashboard.pbix → Power BI visuals
  ↓
.github/workflows/pipeline.yml → automation
```

---

## 📊 Examples of SQL Analysis

* Jobs per company
* Average salary per position
* Job trends over time

---

## ⚙️ CI/CD

* Monthly or manual pipeline runs
* Updates raw, processed, and warehouse data
* Pushes changes to GitHub

---

## 🌱 Future Plans

* Add more dimensions (location, job type, experience)
* Deploy to cloud database
* Live dashboards with real-time updates
* Integrate more job APIs

---

## 👤 Author

**Apurva** – Data Engineering Student
Skills: Python ETL, API ingestion, SQL, Data Warehousing, Power BI, CI/CD

---

✅ This version is **lighter, scannable, and uses visuals/flow diagrams** instead of huge paragraphs or dense bullet lists.

If you want, I can also make a **super “GitHub ready” version with emojis for each step and a neat horizontal pipeline diagram**—it looks way more like a polished project page.

Do you want me to do that?


Overview

This project demonstrates an end-to-end Data Engineering pipeline for collecting, transforming, and analyzing job postings.
All data is ingested via an API (no web scraping), cleaned, and loaded into a SQLite Data Warehouse following a star schema.


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




Author

Apurva – Data Engineering Student

Skills demonstrated: Python ETL pipelines, API data ingestion, data warehouse modeling, SQL analysis, Power BI dashboards, CI/CD automation.
