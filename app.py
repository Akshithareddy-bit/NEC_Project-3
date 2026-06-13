import streamlit as st

st.set_page_config(page_title="AI Healthcare System", layout="wide")

# ---------------------------
# SESSION INIT
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------------------
# WELCOME PAGE
# ---------------------------
if not st.session_state.logged_in:

    st.title("🏥 AI-Powered Healthcare System")

    st.markdown("""
    ## 👋 Welcome to Smart Hospital Management System

    This system helps hospitals manage:

    - 👨‍⚕️ Doctors & Patients
    - 📅 Appointments
    - 🏥 Bed Management
    - 📊 Resource Tracking
    - 🤖 AI Disease Prediction
    - 📄 Electronic Health Records (EHR)

    ---
    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login"):
            st.switch_page("pages/1_Login.py")

    with col2:
        if st.button("📝 Register"):
            st.switch_page("pages/1_Login.py")

    st.stop()

# ---------------------------
# AFTER LOGIN DASHBOARD
# ---------------------------
st.sidebar.title("🏥 Navigation")

st.sidebar.success(f"Logged in as: {st.session_state.username}")
st.sidebar.info(f"Role: {st.session_state.role}")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

st.title("🏠 Dashboard")

st.markdown("### Select a module from sidebar 👈")