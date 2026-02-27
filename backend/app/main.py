from fastapi import FastAPI
from app.routes import cities, wards, temperature, vegetation, builtup, population, predictions, admin, report, gemini
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Urban Heat Island Intelligence Platform (UHI-IP)", description="Detects, predicts, and mitigates Urban Heat Island effects.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cities.router)
app.include_router(wards.router)
app.include_router(temperature.router)
app.include_router(vegetation.router)
app.include_router(builtup.router)
app.include_router(population.router)
app.include_router(predictions.router)
app.include_router(admin.router)
app.include_router(report.router)
app.include_router(gemini.router)
