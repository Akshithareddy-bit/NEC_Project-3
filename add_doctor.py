import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

# USERS (LOGIN)
cursor.execute("INSERT INTO users(username,password,role) VALUES ('admin','admin','Admin')")
cursor.execute("INSERT INTO users(username,password,role) VALUES ('doctor1','1234','Doctor')")
cursor.execute("INSERT INTO users(username,password,role) VALUES ('patient1','1234','Patient')")

# DOCTORS TABLE
cursor.execute("""
INSERT INTO doctors (username, name, specialization, experience)
VALUES ('doctor1', 'Dr Ravi Kumar', 'Cardiology', 5)
""")

conn.commit()
conn.close()

print("Sample data inserted successfully")