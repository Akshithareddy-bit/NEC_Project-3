import sqlite3

conn = sqlite3.connect("database/healthcare.db")
cursor = conn.cursor()

print("\nPATIENTS TABLE:")
cursor.execute("PRAGMA table_info(patients)")
print(cursor.fetchall())

print("\nDOCTORS TABLE:")
cursor.execute("PRAGMA table_info(doctors)")
print(cursor.fetchall())

print("\nAPPOINTMENTS TABLE:")
cursor.execute("PRAGMA table_info(appointments)")
print(cursor.fetchall())

conn.close()