from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Truth Guard API")

# Load the model
MODEL_PATH = "truth_guard_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Warning: Model file '{MODEL_PATH}' not found. Please run train_model.py first.")
    model = None

class NewsRequest(BaseModel):
    text: str

@app.post("/api/predict")
async def predict(request: NewsRequest):
    if model is None:
        return {"prediction": "Error", "message": "Model not loaded. Please train the model first.", "confidence": 0.0}
    
    text = request.text.strip()
    if not text:
        return {"prediction": "Unknown", "message": "Please provide some text.", "confidence": 0.0}

    # Predict probability
    probs = model.predict_proba([text])[0]
    fake_prob = probs[1]
    
    # Threshold for Fake News
    prediction = "Fake News" if fake_prob > 0.5 else "Real News"
    
    return {
        "prediction": prediction,
        "confidence": float(fake_prob if fake_prob > 0.5 else 1 - fake_prob) * 100,
        "message": f"Based on my analysis, I am highly confident this is {prediction.lower()}."
    }

# Mount static files for the frontend
# Ensure static directory exists
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/", StaticFiles(directory="static", html=True), name="static")
