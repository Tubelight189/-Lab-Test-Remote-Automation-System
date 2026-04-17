import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arnav@01012005",
    database="lab_automation"
)

cursor = conn.cursor()

# Read CSV in chunks (IMPORTANT for large data)
chunk_size = 100000

for chunk in pd.read_csv("/home/kiit/lab_automation/data/processing/cleaned_lab_results.csv", chunksize=chunk_size):

    for _, row in chunk.iterrows():
        cursor.execute("""
            INSERT INTO staging_lab_data 
            (hospital, patient_id, test_name, test_value, unit, reference_range, collection_date, is_anomaly)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["hospital"],
            int(row["patient_id"]),
            row["test_name"],
            float(row["test_value"]),
            row["unit"],
            row["reference_range"],
            row["collection_date"],
            bool(row["is_anomaly"])
        ))

    conn.commit()
    print("Chunk inserted")

cursor.close()
conn.close()

print("✅ All data inserted!")
