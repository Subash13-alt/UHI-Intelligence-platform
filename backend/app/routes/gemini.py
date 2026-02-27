# Example usage in FastAPI route
from fastapi import APIRouter, HTTPException
from app.services.gemini import call_gemini_api

router = APIRouter(prefix="/gemini", tags=["Gemini AI"])

@router.post("/generate")
def generate_text(prompt: str):
    try:
        result = call_gemini_api(prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
