import requests
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from app.db import SessionLocal
from app.models import Ward


def fetch_external_data(ward_name: str):
    """
    Simulated external API call.
    Replace with real NASA / NDVI / Population APIs later.
    """

    # Example: Simulated data (replace with real API logic)
    simulated_data = {
        "temperature": round(30 + hash(ward_name) % 7 + 0.5, 2),
        "ndvi": round(0.15 + (hash(ward_name) % 40) / 100, 2),
        "builtup_index": round(0.4 + (hash(ward_name) % 50) / 100, 2),
        "population_density": 10000 + (hash(ward_name) % 20000),
    }

    return simulated_data


def update_all_data():
    """
    Fetch latest environmental data and update database.
    """

    db = SessionLocal()

    try:
        wards = db.query(Ward).all()

        for ward in wards:
            data = fetch_external_data(ward.name)

            ward.temperature = data["temperature"]
            ward.ndvi = data["ndvi"]
            ward.builtup_index = data["builtup_index"]
            ward.population_density = data["population_density"]
            ward.last_updated = datetime.utcnow()

        db.commit()

        return {
            "status": "success",
            "updated_wards": len(wards),
            "timestamp": datetime.utcnow()
        }

    except SQLAlchemyError as e:
        db.rollback()
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        db.close()