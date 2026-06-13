import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

# ---------------------------
# PATIENTS TABLE (FIXED)
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

# ---------------------------
# DOCTORS TABLE
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

# ---------------------------
# APPOINTMENTS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_username TEXT,
    doctor_username TEXT,
    appointment_date TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

# ---------------------------
# EHR TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS ehr (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_username TEXT,
    doctor_username TEXT,
    diagnosis TEXT,
    prescription TEXT,
    notes TEXT,
    visit_date TEXT
)
""")

# ---------------------------
# BEDS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS beds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bed_type TEXT,
    total INTEGER,
    occupied INTEGER
)
""")

# ---------------------------
# RESOURCES TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_name TEXT,
    total_quantity INTEGER,
    used_quantity INTEGER
)
""")

conn.commit()
conn.close()

print("✅ All Tables Created Successfully")