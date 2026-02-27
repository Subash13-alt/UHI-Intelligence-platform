import joblib
import numpy as np

def load_model():
    return joblib.load('uhi_rf_model.joblib')

def predict_heat_score(features):
    model = load_model()
    prediction = model.predict(np.array([features]))
    return float(prediction[0])
