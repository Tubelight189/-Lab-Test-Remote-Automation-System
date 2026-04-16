INSERT INTO dim_hospital (hospital_name)
SELECT DISTINCT hospital
FROM staging_lab_data;
INSERT INTO dim_patient (patient_id)
SELECT DISTINCT patient_id
FROM staging_lab_data;
INSERT INTO dim_test (test_name, unit, reference_range)
SELECT DISTINCT test_name, unit, reference_range
FROM staging_lab_data;

INSERT INTO fact_lab_results (
    patient_id, test_id, hospital_id, test_value, collection_date, is_anomaly
)
SELECT 
    s.patient_id,
    t.test_id,
    h.hospital_id,
    s.test_value,
    s.collection_date,
    s.is_anomaly
FROM staging_lab_data s
JOIN dim_test t 
    ON s.test_name = t.test_name
JOIN dim_hospital h 
    ON s.hospital = h.hospital_name;
    
SELECT patient_id, AVG(test_value)
FROM fact_lab_results
GROUP BY patient_id;

SELECT *
FROM fact_lab_results
WHERE collection_date >= CURDATE() - INTERVAL 30 DAY;

SELECT *
FROM fact_lab_results
WHERE is_anomaly = TRUE;

CREATE INDEX idx_patient ON fact_lab_results(patient_id);
CREATE INDEX idx_test ON fact_lab_results(test_id);