import pandas as pd

df = pd.read_csv("/home/kiit/lab_automation/data/processing/cleaned_lab_results.csv")

anomalies = df[df["is_anomaly"] == True]

df.to_csv("/home/kiit/lab_automation/data/output/flagged_anomalies.csv", index=False)

print("Anomalies extracted:", len(anomalies))
