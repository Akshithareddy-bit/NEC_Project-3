import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# Ensure table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS beds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bed_type TEXT,
    total INTEGER,
    occupied INTEGER
)
""")
conn.commit()

st.title("🏥 Bed Management System")

# -------------------------
# ADD BED DATA
# -------------------------
st.subheader("➕ Add/Update Beds")

bed_type = st.selectbox("Bed Type", ["General", "ICU", "Emergency"])
total = st.number_input("Total Beds", min_value=0)
occupied = st.number_input("Occupied Beds", min_value=0)

if st.button("Save Bed Info"):

    cursor.execute("""
    INSERT INTO beds (bed_type, total, occupied)
    VALUES (?, ?, ?)
    """, (bed_type, total, occupied))

    conn.commit()
    st.success("Bed data saved successfully")

# -------------------------
# DISPLAY BED STATUS
# -------------------------
st.subheader("📊 Current Bed Status")

df = pd.read_sql_query("SELECT * FROM beds", conn)

if not df.empty:
    df["Available"] = df["total"] - df["occupied"]
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bed data available")

conn.close()