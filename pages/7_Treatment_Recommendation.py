import streamlit as st
from utils.recommendation import get_recommendation

st.title("💊 Treatment Recommendation System")

disease = st.selectbox(
    "Select Predicted Disease",
    ["Normal", "Diabetes", "Heart Risk"]
)

if st.button("Get Recommendation"):

    result = get_recommendation(disease)

    st.subheader("👨‍⚕️ Recommended Doctor")
    st.write(result["doctor"])

    st.subheader("🧪 Suggested Tests")
    st.write(result["tests"])

    st.subheader("💊 Medicines")
    st.write(result["medicines"])

    st.subheader("🧾 Health Advice")
    st.write(result["advice"])