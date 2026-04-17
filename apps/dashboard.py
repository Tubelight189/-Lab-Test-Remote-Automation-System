import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="AetherData Lab Analytics", layout="wide")

# Dashboard Title
st.title("🏥 Clinical Lab Test Analytics Dashboard")
st.markdown("Automated pipeline monitoring for patient lab results and anomaly detection.")

# Load Data (Simulating reading from your Parquet/CSV outputs)
# Replace with your actual file paths (e.g., "../data/output/flagged_anomalies.csv")
@st.cache_data
def load_data():
    # Loading the clean data for trends
    df = pd.read_csv("../data/processing/cleaned_lab_results.csv")
    df['collection_date'] = pd.to_datetime(df['collection_date'])
    return df

df = load_data()

# --- Top Metric Cards ---
col1, col2, col3 = st.columns(3)
total_tests = len(df)
anomalies_count = len(df[df['is_anomaly'] == True])
anomaly_rate = (anomalies_count / total_tests) * 100

col1.metric("Total Tests Processed", f"{total_tests:,}")
col2.metric("Anomalies Detected", f"{anomalies_count:,}")
col3.metric("System Anomaly Rate", f"{anomaly_rate:.2f}%")

st.divider()

# --- Interactive Filters ---
st.sidebar.header("Filter Lab Data")
selected_test = st.sidebar.selectbox("Select Test Type", df['test_name'].unique())
show_anomalies_only = st.sidebar.checkbox("Show Flagged Anomalies Only")

# Apply Filters
filtered_df = df[df['test_name'] == selected_test]
if show_anomalies_only:
    filtered_df = filtered_df[filtered_df['is_anomaly'] == True]

# --- Visualization: Trends & Anomalies ---
st.subheader(f"Patient Trends: {selected_test}")

# Create an interactive scatter/line plot using Plotly
fig = px.scatter(
    filtered_df, 
    x="collection_date", 
    y="test_value", 
    color="is_anomaly",
    title=f"{selected_test} Results Over Time",
    labels={"test_value": "Recorded Value", "collection_date": "Date"},
    hover_data=["patient_id", "reference_range"]
)
# Update layout for better visibility
fig.update_traces(marker=dict(size=8))
st.plotly_chart(fig, use_container_width=True)

# --- Raw Data Table ---
st.subheader("Actionable Records (Quarantine Zone)")
st.dataframe(filtered_df.sort_values(by="collection_date", ascending=False).head(100))
