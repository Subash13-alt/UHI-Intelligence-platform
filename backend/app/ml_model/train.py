import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load historical data (simulate or load from DB)
data = pd.read_csv('sample_temperature_data.csv')

features = ['avg_temperature', 'ndvi_score', 'builtup_index', 'population_density']
target = 'heat_score'

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

r2 = r2_score(y_test, model.predict(X_test))
print(f'R2 Score: {r2}')

joblib.dump(model, 'uhi_rf_model.joblib')
