SELECT c.company_name, AVG(f.avg_salary) as mean_pay
FROM fact_jobs f
JOIN dim_company c ON f.company_id = c.company_id
GROUP BY 1 ORDER BY 2 DESC LIMIT 5;
SELECT posted_date, COUNT(*) as volume 
FROM fact_jobs 
GROUP BY 1 ORDER BY 1 ASC;
-- Query: Find the average salary across the top 10 most active companies
SELECT 
    c.company_name, 
    COUNT(f.job_id) as total_jobs,
    ROUND(AVG(f.avg_salary), 2) as avg_pay
FROM fact_jobs f
JOIN dim_company c ON f.company_id = c.company_id
GROUP BY c.company_name
HAVING avg_pay > 0
ORDER BY total_jobs DESC
LIMIT 10;