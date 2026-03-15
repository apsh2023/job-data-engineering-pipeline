-- database/schema.sql

-- 1. Dimension: Companies
CREATE TABLE IF NOT EXISTS dim_company (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT UNIQUE
);

-- 2. Dimension: Tags
CREATE TABLE IF NOT EXISTS dim_tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name TEXT UNIQUE
);

-- 3. Fact Table: Job Postings
CREATE TABLE IF NOT EXISTS fact_jobs (
    fact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER UNIQUE,
    company_id INTEGER,
    position TEXT,
    min_salary INTEGER,
    max_salary INTEGER,
    avg_salary FLOAT,
    posted_date DATE,
    url TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Production Touch: Metadata
    FOREIGN KEY (company_id) REFERENCES dim_company(company_id)
);