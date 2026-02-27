# Placeholder for route modules
# Each file will define FastAPI routers for its domain
"""
Route Package Initializer
Imports all routers so they can be included in main.py
"""

from .city_routes import router as city_router
from .ward_routes import router as ward_router
from .prediction_routes import router as prediction_router
from .analytics_routes import router as analytics_router

__all__ = [
    "city_router",
    "ward_router",
    "prediction_router",
    "analytics_router",
]