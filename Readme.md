🏥 Lab Test Data Engineering Pipeline & Analytics Dashboard
📌 Overview
This project implements an end-to-end data engineering pipeline for processing and analyzing large-scale clinical lab data, along with an interactive analytics dashboard for real-time insights.
It simulates a real-world healthcare data system where data is generated, processed, stored, analyzed, and finally visualized for decision-making.

🚀 Key Features
🔄 Fully automated pipeline using Apache Airflow
📊 Star Schema-based data warehouse
⚡ Big data processing with PySpark
📁 Optimized storage using Parquet
🧹 Data cleaning & normalization
🚨 Anomaly detection system
📈 Interactive dashboard using Streamlit + Plotly

⚙️ Pure Process ka Flow
Data Generate → Move → Clean → Store → Transform → Analyze → Validate → Automate

🏗️ Architecture
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
📊 Streamlit Dashboard (Visualization Layer)


📊 Dashboard (NEW 🔥)
An interactive dashboard built using Streamlit + Plotly to monitor pipeline output and analyze lab results.
🎯 Features
📌 KPI Cards:
Total Tests Processed
Anomalies Detected
Anomaly Rate
🎛️ Filters:
Select test type (e.g., HbA1c)
Toggle anomaly-only view
📈 Visualization:
Time-series scatter plot of lab values
Anomalies highlighted in real-time
📋 Data Table:
Displays latest actionable records
Helps in identifying abnormal cases

🧩 Project Phases
🔹 Phase 1: Data Ingestion & Simulation
Generated synthetic lab data
Automated file movement using shell scripts
Implemented logging
🔹 Phase 2: Data Modeling & Storage
Designed Star Schema:
fact_lab_results
dim_patient, dim_test, dim_hospital
Built ETL pipeline
Loaded ~1.4M records into MySQL
🔹 Phase 3: Big Data Processing
Used PySpark for large-scale processing
Implemented window functions (rolling averages)
Stored optimized data in Parquet format
🔹 Phase 4: Orchestration & Automation
Built Airflow DAG (lab_test_pipeline)
Automated entire workflow
Implemented anomaly detection

⚙️ Technologies Used
Python
Pandas
PySpark
MySQL
Apache Airflow
Streamlit
Plotly
Shell Scripting

📂 Project Structure
project/
│
├── data/
│   	├── landing/
│   	├── processing/
│   	└── output/
│
├── scripts/
│  	 ├── data_generator.py
│   	├── cleaner.py
│   	├── spark_processor.py
│   	├── anomaly_detector.py
│   	└── load_to_mysql.py
│
├── dashboard/
│	   └── app.py
│
├── airflow/
│ 	  └── dag_lab_pipeline.py
│
├── logs/
│	└── ingestion.log
│
├──  sq/l
│	├── Create_tables.sql
│	├── analytics_queries.sql
│	└── insert_dimensions.sql
│
└── README.md


📊 Outputs
✅ Structured MySQL warehouse (Fact + Dimensions)
✅ Parquet files (partitioned, optimized)
✅ Analytical metrics (averages, trends)
✅ flagged_anomalies.csv
✅ 📊 Live dashboard for visualization

▶️ How to Run
1. Run Airflow
airflow webserver --port 8080
airflow scheduler

2. Trigger Pipeline
Open: http://localhost:8080
Run DAG: lab_test_pipeline
3. Run Dashboard
streamlit run dashboard/app.py


🔍 Validation
MySQL:
SELECT COUNT(*) FROM fact_lab_results;

Parquet:
data/output/lab_results_parquet/

Anomalies:
flagged_anomalies.csv


💡 Key Learnings
Built a production-grade data pipeline
Worked with 1.4M+ records
Implemented ETL + Big Data processing
Learned Airflow orchestration
Developed data visualization dashboard

🎯 Conclusion
This project demonstrates a complete data engineering workflow with a visualization layer, transforming raw healthcare data into actionable insights through automation, scalability, and interactive analytics.

👨‍💻 Author
Arnav Adarsh
