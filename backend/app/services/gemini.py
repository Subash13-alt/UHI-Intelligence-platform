import os
import requests

gemini_api_key = os.getenv("GEMINI_API_KEY")

def call_gemini_api(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta2/models/gemini-pro:generateText"
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": {"text": prompt},
        "model": "gemini-pro"
    }
    params = {"key": gemini_api_key}
    response = requests.post(url, json=payload, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
