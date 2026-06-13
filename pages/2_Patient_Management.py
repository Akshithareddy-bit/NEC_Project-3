import streamlit as st
import sqlite3
import pandas as pd

# ---------------------------
# LOGIN CHECK
# ---------------------------
if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state.username
role = st.session_state.role

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------------------
# TABLE CREATE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    doctor_username TEXT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    blood_group TEXT,
    weight REAL,
    height REAL,
    medical_history TEXT,
    allergies TEXT
)
""")
conn.commit()

# ---------------------------
# UI HEADER
# ---------------------------
st.title("🏥 Patient Management System")

st.sidebar.success(f"Logged in as: {user} ({role})")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# ---------------------------
# ADD PATIENT FORM
# ---------------------------
st.subheader("➕ Add New Patient")

with st.form("patient_form"):

    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=1, max_value=120, value=25)

    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

    weight = st.number_input("Weight (kg)", value=60.0)
    height = st.number_input("Height (cm)", value=170.0)

    medical_history = st.text_area("Medical History")
    allergies = st.text_area("Allergies")

    doctor_username = st.text_input("Doctor Username")

    submit = st.form_submit_button("Save Patient")

# ---------------------------
# INSERT DATA
# ---------------------------
if submit:

    if name.strip() == "":
        st.error("Patient Name is required")

    else:
        cursor.execute("""
        INSERT INTO patients (
            username,
            doctor_username,
            name,
            age,
            gender,
            blood_group,
            weight,
            height,
            medical_history,
            allergies
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user,
            doctor_username,
            name,
            age,
            gender,
            blood_group,
            weight,
            height,
            medical_history,
            allergies
        ))

        conn.commit()
        st.success("Patient added successfully!")

# ---------------------------
# SHOW DATA (ROLE BASED)
# ---------------------------
st.subheader("📋 Patient Records")

if role == "Admin":
    df = pd.read_sql_query("SELECT * FROM patients", conn)

elif role == "Doctor":
    df = pd.read_sql_query(
        "SELECT * FROM patients WHERE doctor_username=?",
        conn,
        params=(user,)
    )

else:  # Patient
    df = pd.read_sql_query(
        "SELECT * FROM patients WHERE username=?",
        conn,
        params=(user,)
    )

if len(df) > 0:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No records found")

# ---------------------------
# CLOSE DB
# ---------------------------
conn.close()