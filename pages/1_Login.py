import streamlit as st
import sqlite3

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Healthcare System Login")

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
conn = sqlite3.connect("database/healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------------------
# USERS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")
conn.commit()

# ---------------------------
# OPTION
# ---------------------------
option = st.radio("Select Option", ["Login", "Register"])

# ===========================
# REGISTER
# ===========================
if option == "Register":

    st.subheader("📝 Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Admin", "Doctor", "Patient"])

    if st.button("Register"):

        if username.strip() == "" or password.strip() == "":
            st.error("Username and Password cannot be empty")

        else:
            try:
                cursor.execute("""
                INSERT INTO users(username, password, role)
                VALUES (?, ?, ?)
                """, (username, password, role))

                conn.commit()
                st.success("Registration Successful ✅")

            except sqlite3.IntegrityError:
                st.error("Username already exists ❌")

# ===========================
# LOGIN
# ===========================
else:

    st.subheader("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        cursor.execute("""
        SELECT username, role FROM users
        WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        if user:

            st.session_state.logged_in = True
            st.session_state.username = user[0]
            st.session_state.role = user[1]

            st.success(f"Welcome {user[0]} ({user[1]}) 🎉")

            # AUTO REDIRECT TO APP
            st.switch_page("app.py")

        else:
            st.error("Invalid Username or Password ❌")

conn.close()