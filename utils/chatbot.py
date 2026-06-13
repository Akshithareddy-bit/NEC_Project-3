def chatbot_response(user_input):

    user_input = user_input.lower()

    if "fever" in user_input:
        return "You may have viral fever. Consult a General Physician and take rest + fluids."

    elif "diabetes" in user_input:
        return "Diabetes requires Endocrinologist consultation. Monitor sugar levels regularly."

    elif "heart" in user_input:
        return "Heart-related issues should be checked by a Cardiologist immediately."

    elif "appointment" in user_input:
        return "Go to Appointment page to book or view doctor slots."

    elif "doctor" in user_input:
        return "We have General Physicians, Cardiologists, and Endocrinologists available."

    elif "emergency" in user_input:
        return "In emergency cases, contact hospital immediately or use Emergency Alert System."

    else:
        return "I am a basic healthcare assistant. Please consult a doctor for detailed diagnosis."