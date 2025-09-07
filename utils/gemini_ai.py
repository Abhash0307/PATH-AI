from dotenv import load_dotenv
import os

import requests

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_career_advice(query: str) -> str:
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    body = {
        "contents": [
            {
                "parts": [{"text": query}]
            }
        ]
    }
    response = requests.post(endpoint, headers=headers, params=params, json=body)
    response.raise_for_status()
    result = response.json()
    return result["candidates"][0]["content"]["parts"][0]["text"]
