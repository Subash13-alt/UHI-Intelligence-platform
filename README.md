# Urban Heat Island Intelligence Platform (UHI-IP)

## Overview
A climate analytics system to detect, predict, and mitigate Urban Heat Island effects using satellite data, geospatial analytics, and machine learning.

### Why UHI is Critical in Indian Cities
- Indian cities face extreme heat due to dense infrastructure, low vegetation, and high population.
- UHI increases heatstroke risk, energy consumption, public health threats, and infrastructure stress.

### Data Justification
- Land Surface Temperature: NASA POWER/Open-Meteo
- Vegetation Index: Sentinel-2/NASA MODIS
- Built-up Area: OpenStreetMap/GHSL
- Population Density: WorldPop/Census

### ML Model Choice
- RandomForestRegressor: Robust for tabular, non-linear climate data
- Features: Temperature, NDVI, Built-up, Population

### Scalability Approach
- Dockerized microservices
- PostgreSQL with PostGIS for spatial queries
- Modular FastAPI backend, React frontend
- Compatible with Render, Railway, AWS

### Future Expansion
- IoT sensor integration
- Smart city API interoperability

---

## Setup Instructions

1. Clone repo
2. Add `.env` files (see backend/.env)
3. Run `docker-compose up --build`
4. Access backend: http://localhost:8000 (Swagger docs at /docs)
5. Access frontend: http://localhost:3000

### PostgreSQL/PostGIS Setup
- Uses official PostGIS Docker image
- DB auto-created via docker-compose

### API Documentation
- FastAPI auto-generates Swagger docs

### Sample Data
- ML module uses `sample_temperature_data.csv` for training

---

## Judge Defense Section

- UHI is a major urban health and infrastructure challenge in India
- Data sources are open, reliable, and scalable
- ML model is chosen for interpretability and performance
- System is modular, scalable, and ready for future smart city integrations

---

## Environment Variables
See `backend/.env` for all required keys.

---

## License
MIT
