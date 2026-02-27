# Placeholder for ML model scripts
# Will include training, prediction, and joblib save/load
"""
Urban Heat Island Intelligence Platform
Machine Learning Module
Handles:
- Model training
- Prediction
- Save / Load using joblib
"""

import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

MODEL_PATH = "uhi_model.pkl"


# --------------------------------------------------
# 1️⃣ Synthetic Training Dataset
# Features:
# [current_temp, ndvi, builtup_index, population_density]
# Target:
# future_heat_score (5-year projection)
# --------------------------------------------------

def generate_training_data():
    np.random.seed(42)

    data = []
    targets = []

    for _ in range(100):
        temp = np.random.uniform(30, 37)  # Avg temp range
        ndvi = np.random.uniform(0.1, 0.6)  # Vegetation index
        builtup = np.random.uniform(0.4, 0.9)
        population = np.random.uniform(8000, 30000)

        # Logical heat formula (synthetic but realistic)
        future_heat = (
            0.5 * temp +
            20 * (1 - ndvi) +
            15 * builtup +
            0.0005 * population
        )

        data.append([temp, ndvi, builtup, population])
        targets.append(future_heat)

    return np.array(data), np.array(targets)


# --------------------------------------------------
# 2️⃣ Train Model
# --------------------------------------------------

def train_model():
    X, y = generate_training_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)

    print(f"Model trained successfully")
    print(f"R² Score: {score:.3f}")

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved at {MODEL_PATH}")

    return model


# --------------------------------------------------
# 3️⃣ Load Model
# --------------------------------------------------

def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully")
        return model
    except FileNotFoundError:
        print("Model not found. Training new model...")
        return train_model()


# --------------------------------------------------
# 4️⃣ Predict Future Heat Score
# --------------------------------------------------

def predict_heat(temp, ndvi, builtup, population):
    model = load_model()

    input_data = np.array([[temp, ndvi, builtup, population]])
    prediction = model.predict(input_data)

    return round(float(prediction[0]), 2)


# --------------------------------------------------
# 5️⃣ Example Usage
# --------------------------------------------------

if __name__ == "__main__":
    model = train_model()

    # Example: T Nagar-like conditions
    predicted_score = predict_heat(
        temp=35.6,
        ndvi=0.18,
        builtup=0.82,
        population=28500
    )

    print(f"Predicted 5-Year Heat Score: {predicted_score}")