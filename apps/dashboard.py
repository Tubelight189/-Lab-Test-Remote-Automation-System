import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="LabFlow Analytics", layout="wide")

# Dashboard Title
st.title("🏥 LabFlow Analytics Dashboard")
st.markdown("End-to-end clinical data pipeline monitoring with real-time anomaly detection and insights.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/processing/cleaned_lab_results.csv")
    df['collection_date'] = pd.to_datetime(df['collection_date'])
    return df

df = load_data()

# --- Top Metric Cards ---
col1, col2, col3 = st.columns(3)

total_tests = len(df)
anomalies_count = len(df[df['is_anomaly'] == True])
anomaly_rate = (anomalies_count / total_tests) * 100 if total_tests > 0 else 0

col1.metric("Total Tests Processed", f"{total_tests:,}")
col2.metric("Anomalies Detected", f"{anomalies_count:,}")
col3.metric("Anomaly Rate", f"{anomaly_rate:.2f}%")

st.divider()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Data")

selected_test = st.sidebar.selectbox(
    "Select Test Type",
    sorted(df['test_name'].unique())
)

show_anomalies_only = st.sidebar.checkbox("Show Only Anomalies")

# Apply Filters
filtered_df = df[df['test_name'] == selected_test]

if show_anomalies_only:
    filtered_df = filtered_df[filtered_df['is_anomaly'] == True]

# --- Visualization ---
st.subheader(f"📈 Trends for {selected_test}")

fig = px.scatter(
    filtered_df,
    x="collection_date",
    y="test_value",
    color="is_anomaly",
    title=f"{selected_test} Results Over Time",
    labels={
        "test_value": "Test Value",
        "collection_date": "Date"
    },
    hover_data=["patient_id", "reference_range"]
)

fig.update_traces(marker=dict(size=8))

st.plotly_chart(fig, use_container_width=True)

# --- Data Table ---
st.subheader("📋 Recent Records (Anomaly Monitoring)")

st.dataframe(
    filtered_df
    .sort_values(by="collection_date", ascending=False)
    .head(100)
)
