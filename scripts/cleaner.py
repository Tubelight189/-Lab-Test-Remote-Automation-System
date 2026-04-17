import pandas as pd

# Load data
df = pd.read_csv("/home/kiit/lab_automation/data/processing/large_lab_results.csv")
# ----------------------------
# 1. Standardize Test Names
# ----------------------------
test_mapping = {
    "Hemoglobin A1c": "HbA1c",
    "HbA1c": "HbA1c",
    "Glycated Hemoglobin": "HbA1c",
    
    "Cholesterol": "Cholesterol",
    "Total Chol": "Cholesterol",
    "Serum Cholesterol": "Cholesterol",
    
    "Glucose": "Glucose",
    "Blood Sugar": "Glucose"
}

df["test_name"] = df["test_name"].map(test_mapping)

# ----------------------------
# 2. Unit Normalization
# ----------------------------

def convert_glucose(row):
    if row["test_name"] == "Glucose" and row["unit"] == "mmol/L":
        return row["test_value"] * 18  # convert to mg/dL
    return row["test_value"]

df["test_value"] = df.apply(convert_glucose, axis=1)

# Convert unit column
df.loc[df["test_name"] == "Glucose", "unit"] = "mg/dL"

# ----------------------------
# 3. Handle Missing Values
# ----------------------------
df = df.dropna()

# ----------------------------
# 4. Save Clean Data
# ----------------------------
df.to_csv("/home/kiit/lab_automation/data/processing/cleaned_lab_results.csv", index=False)

print("✅ Data cleaned and saved!")
