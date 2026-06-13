import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state.username
role = st.session_state.role

conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

st.title("📅 Appointment System")

# ---------------------------
# GET DOCTORS FROM DB
# ---------------------------
doctors = pd.read_sql_query("SELECT username FROM doctors", conn)
doctor_list = doctors["username"].tolist() if not doctors.empty else []

# ---------------------------
# GET PATIENTS FROM DB
# ---------------------------
patients = pd.read_sql_query("SELECT username FROM patients", conn)
patient_list = patients["username"].tolist() if not patients.empty else []

# ---------------------------
# BOOK APPOINTMENT
# ---------------------------
st.subheader("➕ Book Appointment")

with st.form("appt_form"):

    patient_username = st.selectbox("Select Patient", patient_list)
    doctor_username = st.selectbox("Select Doctor", doctor_list)
    appointment_date = st.date_input("Date", value=date.today())

    submit = st.form_submit_button("Book")

if submit:

    cursor.execute("""
    INSERT INTO appointments (
        patient_username,
        doctor_username,
        appointment_date
    )
    VALUES (?, ?, ?)
    """, (patient_username, doctor_username, str(appointment_date)))

    conn.commit()
    st.success("Appointment Booked Successfully!")

# ---------------------------
# VIEW APPOINTMENTS
# ---------------------------
st.subheader("📋 Appointments")

if role == "Admin":
    df = pd.read_sql_query("SELECT * FROM appointments", conn)

elif role == "Doctor":
    df = pd.read_sql_query(
        "SELECT * FROM appointments WHERE doctor_username=?",
        conn,
        params=(user,)
    )

else:
    df = pd.read_sql_query(
        "SELECT * FROM appointments WHERE patient_username=?",
        conn,
        params=(user,)
    )

st.dataframe(df, use_container_width=True)