import streamlit as st
from utils.chatbot import chatbot_response

st.title("🤖 AI Healthcare Chatbot")

st.write("Ask basic health-related questions below:")

user_input = st.text_input("Enter your question")

if st.button("Ask AI"):

    if user_input.strip() == "":
        st.warning("Please enter a question")
    else:
        response = chatbot_response(user_input)
        st.success(response)