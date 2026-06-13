import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)

st.title("📊 Analytics Dashboard")

# ------------------------
# FETCH DATA
# ------------------------
patients = pd.read_sql_query("SELECT * FROM patients", conn)
doctors = pd.read_sql_query("SELECT * FROM doctors", conn)
beds = pd.read_sql_query("SELECT * FROM beds", conn)
resources = pd.read_sql_query("SELECT * FROM resources", conn)

# ------------------------
# METRICS
# ------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", len(patients))
col2.metric("Total Doctors", len(doctors))

total_beds = beds["total"].sum() if not beds.empty else 0
occupied_beds = beds["occupied"].sum() if not beds.empty else 0

col3.metric("Total Beds", total_beds)
col4.metric("Occupied Beds", occupied_beds)

# ------------------------
# BED USAGE CHART
# ------------------------
st.subheader("🛏️ Bed Usage")

if not beds.empty:
    fig, ax = plt.subplots()
    ax.bar(["Total", "Occupied"], [total_beds, occupied_beds])
    st.pyplot(fig)

# ------------------------
# RESOURCE USAGE CHART
# ------------------------
st.subheader("📦 Resource Usage")

if not resources.empty:
    fig2, ax2 = plt.subplots()
    ax2.bar(resources["resource_name"], resources["used_quantity"])
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# ------------------------
# PATIENT OVERVIEW
# ------------------------
st.subheader("👥 Patient Data Preview")
st.dataframe(patients)

conn.close()