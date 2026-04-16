-- CREATE DATABASE lab_automation;
-- USE lab_automation;fact_lab_resultsdim_test
-- Dimension: Hospital
CREATE TABLE dim_hospital (
    hospital_id INT AUTO_INCREMENT PRIMARY KEY,
    hospital_name VARCHAR(50)
);

-- Dimension: Test
CREATE TABLE dim_test (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    test_name VARCHAR(50),
    unit VARCHAR(20),
    reference_range VARCHAR(50)
);

-- Dimension: Patient
CREATE TABLE dim_patient (
    patient_id INT PRIMARY KEY
);

-- Fact Table
CREATE TABLE fact_lab_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    test_id INT,
    hospital_id INT,
    test_value FLOAT,
    collection_date DATE,
    is_anomaly BOOLEAN,

    FOREIGN KEY (patient_id) REFERENCES dim_patient(patient_id),
    FOREIGN KEY (test_id) REFERENCES dim_test(test_id),
    FOREIGN KEY (hospital_id) REFERENCES dim_hospital(hospital_id)
);