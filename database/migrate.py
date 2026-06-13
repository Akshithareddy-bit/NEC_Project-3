import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

# -------------------------
# ADD COLUMNS SAFELY
# -------------------------

def add_column(table, column, col_type):
    try:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
        print(f"Added {column} to {table}")
    except:
        pass

# Patients upgrades
add_column("patients", "username", "TEXT")
add_column("patients", "doctor_username", "TEXT")

# Appointments table ensure
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_username TEXT,
    doctor_username TEXT,
    appointment_date TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()
conn.close()

print("Migration completed safely")