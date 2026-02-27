from app.ml_model.predict import predict_heat_score
from fastapi import APIRouter, HTTPException
from app.db import SessionLocal
from app.models import Ward, TemperatureData, VegetationData, BuiltupData, PopulationData

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/{ward_id}")
def predict_ward_heat(ward_id: int):
    db = SessionLocal()
    try:
        temp = db.query(TemperatureData).filter(TemperatureData.ward_id == ward_id).order_by(TemperatureData.date.desc()).first()
        veg = db.query(VegetationData).filter(VegetationData.ward_id == ward_id).first()
        built = db.query(BuiltupData).filter(BuiltupData.ward_id == ward_id).first()
        pop = db.query(PopulationData).filter(PopulationData.ward_id == ward_id).first()
        if not all([temp, veg, built, pop]):
            raise HTTPException(status_code=404, detail="Missing data for prediction")
        features = [temp.avg_temperature, veg.ndvi_score, built.builtup_index, pop.population_density]
        heat_score = predict_heat_score(features)
        return {"ward_id": ward_id, "predicted_heat_score": heat_score, "confidence": 0.95}
    finally:
        db.close()
