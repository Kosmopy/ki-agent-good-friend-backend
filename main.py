# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class OccasionRequest(BaseModel):
    name: str
    occasion: str
    date: str

@app.post("/generate-message")
async def generate_message(data: OccasionRequest):
    message = f"Hey {data.name}, just a quick note to say happy {data.occasion} on {data.date}! 🎉"
    return {"message": message}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
