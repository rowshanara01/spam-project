"""Step 2: Model ke API banano (FastAPI)"""
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Spam Detector API")

# Next.js (localhost:3000) theke call korte dibe
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model/spam_model.joblib")  # server start e ekbar load


class Message(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(msg: Message):
    spam_prob = float(model.predict_proba([msg.text])[0][1])
    return {
        "label": "spam" if spam_prob >= 0.5 else "ham",
        "spam_probability": round(spam_prob, 4),
    }
