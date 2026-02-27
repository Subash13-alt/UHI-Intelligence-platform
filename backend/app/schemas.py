from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class CityBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class CityOut(CityBase):
    id: int
    class Config:
        orm_mode = True

class WardBase(BaseModel):
    city_id: int
    ward_name: str
    geometry: str

class WardOut(WardBase):
    id: int
    class Config:
        orm_mode = True

class TemperatureDataOut(BaseModel):
    ward_id: int
    date: date
    avg_temperature: float
    max_temperature: float
    class Config:
        orm_mode = True

class VegetationDataOut(BaseModel):
    ward_id: int
    ndvi_score: float
    class Config:
        orm_mode = True

class BuiltupDataOut(BaseModel):
    ward_id: int
    builtup_index: float
    class Config:
        orm_mode = True

class PopulationDataOut(BaseModel):
    ward_id: int
    population_density: float
    class Config:
        orm_mode = True

class PredictionOut(BaseModel):
    ward_id: int
    predicted_heat_score: float
    prediction_year: int
    confidence: float
    class Config:
        orm_mode = True
