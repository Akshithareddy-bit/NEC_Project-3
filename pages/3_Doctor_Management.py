import streamlit as st
import sqlite3
import pandas as pd

# ---------------------------
# LOGIN CHECK
# ---------------------------
if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# ---------------------------
# ROLE CHECK
# ---------------------------
role = st.session_state.get("role", "")
user = st.session_state.get("username", "")

if role not in ["Doctor", "Admin"]:
    st.error("Access Denied ❌ You are not allowed to open this page")
    st.stop()

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------------------
# TITLE
# ---------------------------
st.title("👨‍⚕️ Doctor Management System")

st.sidebar.success(f"Logged in as: {user} ({role})")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# ---------------------------
# CREATE TABLE (SAFE)
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    name TEXT,
    specialization TEXT,
    experience INTEGER
)
""")
conn.commit()

# ---------------------------
# ADD DOCTOR FORM (ADMIN ONLY)
# ---------------------------
if role == "Admin":

    st.subheader("➕ Add Doctor")

    with st.form("doctor_form"):

        doc_username = st.text_input("Doctor Username")
        name = st.text_input("Doctor Name")
        specialization = st.text_input("Specialization")
        experience = st.number_input("Experience (years)", min_value=0)

        submit = st.form_submit_button("Save Doctor")

    if submit:

        if name.strip() == "" or doc_username.strip() == "":
            st.error("Username and Name required")
        else:

            cursor.execute("""
            INSERT INTO doctors (username, name, specialization, experience)
            VALUES (?, ?, ?, ?)
            """,
            (doc_username, name, specialization, experience))

            conn.commit()
            st.success("Doctor Added Successfully!")

# ---------------------------
# VIEW DOCTORS
# ---------------------------
st.subheader("📋 Doctor List")

if role == "Admin":
    df = pd.read_sql_query("SELECT * FROM doctors", conn)

else:
    df = pd.read_sql_query(
        "SELECT * FROM doctors WHERE username=?",
        conn,
        params=(user,)
    )

if len(df) > 0:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No doctor records found")

# ---------------------------
# CLOSE CONNECTION
# ---------------------------
conn.close()