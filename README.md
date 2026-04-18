# 🏥 LabFlow Analytics: Clinical Data Engineering Pipeline & Dashboard

## 📌 Overview

**LabFlow Analytics** is an end-to-end data engineering pipeline designed to process and analyze large-scale clinical lab data, along with an interactive analytics dashboard for real-time insights.

It handles **~1.4M+ records**, simulating real-world healthcare data at scale.

The system follows a complete pipeline:

> **Generated → Ingested → Transformed → Stored → Analyzed → Visualized**

---

## 🚀 Key Features

* 🔄 Fully automated pipeline using **Apache Airflow**
* 📊 **Star Schema**-based data warehouse
* ⚡ Big data processing with **PySpark**
* 📁 Optimized storage using **Parquet**
* 🧹 Data cleaning & normalization
* 🚨 Anomaly detection system
* 📈 Interactive dashboard using **Streamlit + Plotly**
* 🧠 Designed as a production-style modular data pipeline

---

## 🔄 Pipeline Flow

```text
Data Generate → Move → Clean → Store → Transform → Analyze → Validate → Automate
```

---

## 🏗️ Architecture

```text
Data Generation (Python)
        ↓
Landing Folder
        ↓
Shell Script (Ingestion)
        ↓
Processing Folder
        ↓
Data Cleaning (Python)
        ↓
MySQL (Staging + Warehouse)
        ↓
ETL → Star Schema
        ↓
PySpark Processing
        ↓
Parquet Output
        ↓
Anomaly Detection
        ↓
Airflow DAG (Automation)
        ↓
📊 Streamlit Dashboard
```

---

## 📊 LabFlow Analytics Dashboard

An interactive dashboard built using **Streamlit + Plotly** to monitor pipeline output and analyze lab results.

### 🎯 Features

* 📌 **KPI Cards**

  * Total Tests Processed
  * Anomalies Detected
  * Anomaly Rate

* 🎛️ **Filters**

  * Select test type (e.g., HbA1c)
  * Toggle anomaly-only view

* 📈 **Visualization**

  * Time-series scatter plot of lab values
  * Real-time anomaly highlighting

* 📋 **Data Table**

  * Displays latest actionable records
  * Helps identify abnormal cases

---

## 🧩 Project Phases

### 🔹 Phase 1: Data Ingestion & Simulation

* Generated synthetic lab data
* Automated file movement using shell scripts
* Implemented logging

### 🔹 Phase 2: Data Modeling & Storage

* Designed **Star Schema**

  * `fact_lab_results`
  * `dim_patient`, `dim_test`, `dim_hospital`
* Built ETL pipeline
* Loaded **~1.4M records into MySQL**

### 🔹 Phase 3: Big Data Processing

* Used **PySpark** for large-scale processing
* Implemented **window functions (rolling averages)**
* Stored optimized data in **Parquet format**

### 🔹 Phase 4: Orchestration & Automation

* Built **Airflow DAG (`lab_test_pipeline`)**
* Automated the entire workflow
* Integrated anomaly detection

---

## ⚙️ Technologies Used

* Python
* Pandas
* PySpark
* MySQL
* Apache Airflow
* Streamlit
* Plotly
* Shell Scripting

---

## 📂 Project Structure

```text
project/
│
├── data/
│   ├── landing/
│   ├── processing/
│   └── output/
│
├── scripts/
│   ├── data_generator.py
│   ├── cleaner.py
│   ├── spark_processor.py
│   ├── anomaly_detector.py
│   └── load_to_mysql.py
│
├── dashboard/
│   └── app.py
│
├── airflow/
│   └── dag_lab_pipeline.py
│
├── logs/
│   └── ingestion.log
│
├── sql/
│   ├── create_tables.sql
│   ├── analytics_queries.sql
│   └── insert_dimensions.sql
│
└── README.md
```

---

## 🧪 Dataset & Data Simulation

This project uses a **synthetically generated clinical dataset** to simulate real-world healthcare data at scale.

### 📊 Dataset Characteristics
- 📦 Size: ~1.4M+ records  
- 🧍 Entities: Patients, Tests, Hospitals  
- 🧾 Fields include:
  - `patient_id`
  - `test_name` (HbA1c, Glucose, Cholesterol, etc.)
  - `test_value`
  - `collection_date`
  - `reference_range`
  - `hospital_id`
  - `is_anomaly`


### ⚙️ Data Generation
- Data is generated using a custom Python script:
  ```bash
  python scripts/data_generator.py

---

## 📊 Outputs

* ✅ Structured MySQL warehouse (Fact + Dimensions)
* ✅ Parquet files (partitioned, optimized)
* ✅ Analytical metrics (averages, trends)
* ✅ `flagged_anomalies.csv`
* ✅ Live dashboard for visualization

> 📌 Note: Full dataset (~1.4M records) is not included in the repository.
> A sample dataset or data generation script is provided for reproducibility.

---

## ▶️ How to Run

### 1️⃣ Start Airflow

```bash
airflow webserver --port 8080
airflow scheduler
```

### 2️⃣ Trigger Pipeline

* Open: http://localhost:8080
* Run DAG: `lab_test_pipeline`

### 3️⃣ Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 🔍 Validation & Testing

To ensure the integrity and reliability of the data pipeline, the following validation checks can be performed across different layers of the architecture.

---

## 🗄️ 1. MySQL Data Warehouse (Storage Layer)

Verify that records are successfully loaded into the star schema and relationships are correctly maintained.

```sql
-- Total records in Fact Table
SELECT COUNT(*) FROM fact_lab_results;

-- Anomaly count by test type
SELECT t.test_name, COUNT(*) AS anomaly_count
FROM fact_lab_results f
JOIN dim_test t ON f.test_id = t.test_id
WHERE f.is_anomaly = TRUE
GROUP BY t.test_name
ORDER BY anomaly_count DESC;
```

**✔️ Ensures:**
- Data is properly loaded into the warehouse  
- Foreign key relationships are valid  
- Anomaly distribution across test types is logical  

---

## ⚡ 2. PySpark Parquet Output (Big Data Layer)

Validate that the Spark job correctly partitions and stores the data.

```bash
# View partitioned output structure
ls -lh data/output/lab_results_parquet/ | head -n 10
```

**✔️ Success Indicators:**
- Presence of partitioned folders like `collection_date=YYYY-MM-DD/`  
- Confirms efficient data lake design and query optimization  

---

## 🚨 3. Anomaly Detection (Quality Assurance)

Ensure abnormal records are correctly isolated for further analysis.

```bash
# Count total flagged anomalies
wc -l data/output/flagged_anomalies.csv

# Preview top anomaly records
head -n 6 data/output/flagged_anomalies.csv
```

**✔️ Ensures:**
- Anomaly detection logic is working correctly  
- Critical records are captured for review  

---

## 🔄 4. Airflow Orchestration (Automation Validation)

Verify that the pipeline executed successfully without failures.

**Steps:**
1. Open Airflow UI: `http://localhost:8080`
2. Select DAG: `lab_test_pipeline`
3. Navigate to **Graph View**
4. Confirm all tasks show **Success** (green):
   - `generate_data`
   - `clean_and_normalize`
   - `load_to_warehouse`
   - `process_analytics`
   - `flag_anomalies`

**✔️ Ensures:**
- End-to-end pipeline execution is successful  
- No task failures or retries  
- Workflow automation is reliable  

---

## 💡 Key Learnings

* Built a production-grade data pipeline
* Worked with **1.4M+ records**
* Implemented ETL + Big Data processing
* Learned Airflow orchestration
* Developed an interactive data dashboard

---

## 🎯 Conclusion

**LabFlow Analytics** demonstrates a complete data engineering workflow with a visualization layer, transforming raw healthcare data into actionable insights through:

* Automation
* Scalability
* Real-time analytics

---

## 👨‍💻 Author

**Arnav Adarsh**
B.Tech Computer Science  
🔗 GitHub: https://github.com/Tubelight189  
🔗 LinkedIn: https://www.linkedin.com/in/arnav-adarsh-9004632aa/
