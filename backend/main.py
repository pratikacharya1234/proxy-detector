from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model.detector import load_model, detect_text

# Initialize FastAPI app
app = FastAPI(title="AI Text Detector")

# Define request body structure
class TextInput(BaseModel):
    text: str

# Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to AI Text Detector"}

# Detection endpoint
@app.post("/detect")
async def detect(input: TextInput):
    # Validate input
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Load model and predict
    model = load_model()
    prediction = detect_text(model, input.text)
    
    # Return result
    return {
        "result": "human" if prediction["label"] == 0 else "ai",
        "confidence": float(prediction["confidence"])
    }

# Run with: uvicorn backend.main:app --reload