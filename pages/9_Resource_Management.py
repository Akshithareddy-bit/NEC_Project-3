import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# Ensure table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_name TEXT,
    total_quantity INTEGER,
    used_quantity INTEGER
)
""")
conn.commit()

st.title("🏥 Resource Management System")

# -------------------------
# ADD RESOURCE
# -------------------------
st.subheader("➕ Add / Update Resources")

resource_name = st.selectbox(
    "Resource Type",
    ["Oxygen Cylinder", "Ventilator", "ICU Kit", "Surgical Kit"]
)

total_quantity = st.number_input("Total Quantity", min_value=0)
used_quantity = st.number_input("Used Quantity", min_value=0)

if st.button("Save Resource"):

    cursor.execute("""
    INSERT INTO resources (resource_name, total_quantity, used_quantity)
    VALUES (?, ?, ?)
    """, (resource_name, total_quantity, used_quantity))

    conn.commit()
    st.success("Resource data saved successfully")

# -------------------------
# DISPLAY RESOURCES
# -------------------------
st.subheader("📊 Resource Status")

df = pd.read_sql_query("SELECT * FROM resources", conn)

if not df.empty:
    df["Available"] = df["total_quantity"] - df["used_quantity"]
    st.dataframe(df, use_container_width=True)
else:
    st.info("No resource data available")

conn.close()