SELECT patient_id, AVG(test_value) AS avg_value
FROM fact_lab_results
GROUP BY patient_id;

SELECT *
FROM fact_lab_results
WHERE collection_date >= CURDATE() - INTERVAL 30 DAY;

SELECT *
FROM fact_lab_results
WHERE is_anomaly = TRUE;
