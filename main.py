# main.py (FastAPI)

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from urllib.parse import quote
import os

app = FastAPI()

# Load Groq model once
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=2)

class OccasionRequest(BaseModel):
    name: str
    occasion: str
    date: str  # optional, for logging/debug
    phone: str

@app.post("/generate-message")
async def generate_message(data: OccasionRequest):
    prompt = (
        f"Schreibe eine herzliche Nachricht aus der Perspektive eines Freundes für {data.name} zum Anlass ihrer {data.occasion} heute. "
        "Schreibe auf Deutsch, in 1-2 Sätzen und möglichst personalisiert mit Bezug zu {data.occasion}. Schreibe aus der Ich-Perspektive. Vermeide 'wir'. Suggeriere nicht, dass du die Person heute sehen wirst."
    )
    response = model.invoke(prompt)
    message = response.content

    # Spell check
    spell_check_prompt = f"Korrigiere die Rechtschreibung und Grammatik des folgenden deutschen Textes: {message}. Gib nur den korrigierten Text zurück."
    corrected = model.invoke(spell_check_prompt).content

    encoded_message = quote(corrected)
    whatsapp_link = f"https://wa.me/{data.phone}?text={encoded_message}"
    println("✅ Raw response from backend: $responseBodyString")
    return {
        "message": corrected,
        "whatsapp_link": whatsapp_link
    }