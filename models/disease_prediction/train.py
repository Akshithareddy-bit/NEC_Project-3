import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset (you can expand later)
data = {
    "age": [25, 45, 50, 35, 60, 70, 30, 55],
    "bmi": [22, 28, 31, 24, 35, 38, 23, 32],
    "bp": [120, 140, 150, 130, 160, 170, 118, 155],
    "glucose": [90, 150, 160, 100, 180, 200, 95, 170],
    "cholesterol": [180, 220, 240, 190, 260, 280, 175, 250],
    "disease": [
        "Normal",
        "Diabetes",
        "Diabetes",
        "Normal",
        "Heart Risk",
        "Heart Risk",
        "Normal",
        "Heart Risk"
    ]
}

df = pd.DataFrame(data)

X = df[["age", "bmi", "bp", "glucose", "cholesterol"]]
y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "models/disease_prediction/model.pkl")

print("Model Trained and Saved Successfully")