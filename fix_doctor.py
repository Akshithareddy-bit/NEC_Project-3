import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO doctors (username, name, specialization, experience)
VALUES ('doctor1', 'Dr Ravi', 'Cardiology', 5)
""")

conn.commit()
conn.close()

print("Inserted successfully")