import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

# ADMIN
cursor.execute("""
INSERT INTO users (username, password, role)
VALUES ('admin', 'admin', 'Admin')
""")

# DOCTOR
cursor.execute("""
INSERT INTO users (username, password, role)
VALUES ('doctor1', '1234', 'Doctor')
""")

# PATIENT
cursor.execute("""
INSERT INTO users (username, password, role)
VALUES ('patient1', '1234', 'Patient')
""")

# DOCTOR TABLE DATA
cursor.execute("""
INSERT INTO doctors (username, name, specialization, experience)
VALUES ('doctor1', 'Dr Ravi', 'Cardiology', 5)
""")

conn.commit()
conn.close()

print("Sample data added successfully")