import pandas as pd

# Simulated sample dataset for ML training
# Columns: avg_temperature, ndvi_score, builtup_index, population_density, heat_score
sample_data = {
    "avg_temperature": [32.5, 33.1, 34.0, 31.8, 35.2],
    "ndvi_score": [0.25, 0.32, 0.28, 0.35, 0.22],
    "builtup_index": [0.65, 0.70, 0.60, 0.55, 0.75],
    "population_density": [12000, 15000, 11000, 9000, 16000],
    "heat_score": [78, 82, 75, 68, 85]
}
df = pd.DataFrame(sample_data)
df.to_csv('sample_temperature_data.csv', index=False)
