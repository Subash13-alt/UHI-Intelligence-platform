from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from app.db import Base

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    wards = relationship("Ward", back_populates="city")

class Ward(Base):
    __tablename__ = "wards"
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    ward_name = Column(String, nullable=False)
    geometry = Column(Geometry("POLYGON"))
    city = relationship("City", back_populates="wards")

class TemperatureData(Base):
    __tablename__ = "temperature_data"
    id = Column(Integer, primary_key=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    date = Column(Date)
    avg_temperature = Column(Float)
    max_temperature = Column(Float)

class VegetationData(Base):
    __tablename__ = "vegetation_data"
    id = Column(Integer, primary_key=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    ndvi_score = Column(Float)

class BuiltupData(Base):
    __tablename__ = "builtup_data"
    id = Column(Integer, primary_key=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    builtup_index = Column(Float)

class PopulationData(Base):
    __tablename__ = "population_data"
    id = Column(Integer, primary_key=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    population_density = Column(Float)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    predicted_heat_score = Column(Float)
    prediction_year = Column(Integer)
    confidence = Column(Float)
