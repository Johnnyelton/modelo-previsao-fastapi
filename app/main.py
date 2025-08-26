from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Modelo de Previsão (FastAPI)", version="1.0.0")

class PredictIn(BaseModel):
    feature_1: float = Field(..., description="Primeira feature numérica")
    feature_2: float = Field(..., description="Segunda feature numérica")
    feature_3: Optional[float] = Field(None, description="Terceira feature numérica (opcional)")

class PredictOut(BaseModel):
    prediction: str
    score: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictOut)
def predict(payload: PredictIn):
    # Regra simples de 'modelo' para fins de demonstração
    score = 0.7 * payload.feature_1 + 0.3 * payload.feature_2
    if payload.feature_3 is not None:
        score += 0.1 * payload.feature_3

    prediction = "positive" if score >= 1.0 else "negative"
    return {"prediction": prediction, "score": round(score, 4)}
