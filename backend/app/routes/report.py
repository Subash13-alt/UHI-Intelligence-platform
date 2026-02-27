from fastapi import APIRouter, HTTPException
from app.db import SessionLocal
from app.models import Ward, TemperatureData, VegetationData, BuiltupData, PopulationData, Prediction
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/report", tags=["Report"])

@router.get("/generate/{ward_id}")
def generate_report(ward_id: int):
    db = SessionLocal()
    try:
        temp = db.query(TemperatureData).filter(TemperatureData.ward_id == ward_id).order_by(TemperatureData.date.desc()).first()
        veg = db.query(VegetationData).filter(VegetationData.ward_id == ward_id).first()
        built = db.query(BuiltupData).filter(BuiltupData.ward_id == ward_id).first()
        pop = db.query(PopulationData).filter(PopulationData.ward_id == ward_id).first()
        pred = db.query(Prediction).filter(Prediction.ward_id == ward_id).order_by(Prediction.prediction_year.desc()).first()
        if not all([temp, veg, built, pop, pred]):
            raise HTTPException(status_code=404, detail="Missing data for report")
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.drawString(100, 750, f"Urban Heat Island Report for Ward {ward_id}")
        c.drawString(100, 730, f"Current Avg Temp: {temp.avg_temperature}")
        c.drawString(100, 710, f"NDVI Score: {veg.ndvi_score}")
        c.drawString(100, 690, f"Built-up Index: {built.builtup_index}")
        c.drawString(100, 670, f"Population Density: {pop.population_density}")
        c.drawString(100, 650, f"Predicted Heat Score ({pred.prediction_year}): {pred.predicted_heat_score}")
        c.save()
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename=ward_{ward_id}_report.pdf"})
    finally:
        db.close()
