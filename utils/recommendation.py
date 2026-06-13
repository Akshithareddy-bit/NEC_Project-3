def get_recommendation(disease):

    if disease == "Diabetes":
        return {
            "doctor": "Endocrinologist",
            "tests": ["HbA1c", "Fasting Blood Sugar"],
            "medicines": ["Metformin", "Insulin (if severe)"],
            "advice": "Avoid sugar, exercise daily, monitor glucose"
        }

    elif disease == "Heart Risk":
        return {
            "doctor": "Cardiologist",
            "tests": ["ECG", "Echocardiogram", "Cholesterol Test"],
            "medicines": ["Aspirin", "Atorvastatin"],
            "advice": "Low salt diet, avoid stress, regular BP check"
        }

    elif disease == "Normal":
        return {
            "doctor": "General Physician",
            "tests": ["Routine Blood Checkup"],
            "medicines": ["No medication required"],
            "advice": "Maintain healthy lifestyle"
        }

    else:
        return {
            "doctor": "General Physician",
            "tests": ["Further diagnosis required"],
            "medicines": ["Consult doctor"],
            "advice": "More tests needed"
        }