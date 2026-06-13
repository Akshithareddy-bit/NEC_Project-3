import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# Ensure table exists (safety)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ehr (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    diagnosis TEXT,
    prescription TEXT,
    notes TEXT,
    visit_date TEXT
)
""")
conn.commit()

st.title("📋 Electronic Health Record (EHR)")

# -------------------------
# ADD NEW RECORD
# -------------------------
st.subheader("➕ Add Medical Record")

patient_name = st.text_input("Patient Name")
doctor_name = st.text_input("Doctor Name")
diagnosis = st.text_area("Diagnosis")
prescription = st.text_area("Prescription")
notes = st.text_area("Additional Notes")
visit_date = st.date_input("Visit Date", value=date.today())

if st.button("Save Record"):

    if patient_name == "" or doctor_name == "":
        st.error("Patient and Doctor name are required")
    else:
        cursor.execute("""
        INSERT INTO ehr (
            patient_name,
            doctor_name,
            diagnosis,
            prescription,
            notes,
            visit_date
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            patient_name,
            doctor_name,
            diagnosis,
            prescription,
            notes,
            str(visit_date)
        ))

        conn.commit()
        st.success("EHR Record Saved Successfully")

# -------------------------
# VIEW RECORDS
# -------------------------
st.subheader("📄 Medical Records")

df = pd.read_sql_query("SELECT * FROM ehr ORDER BY id DESC", conn)
st.dataframe(df, use_container_width=True)

conn.close()