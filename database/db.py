import sqlite3

def create_connection():
    conn = sqlite3.connect("database/healthcare.db")
    return conn