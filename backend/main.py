from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.detector import load_model, detect_text

# Create FastAPI app
app = FastAPI(title="Proxy Detector", description="AI Text Detector API", version="1.0")

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the model when server starts
model = load_model()

# Define request data model
class TextRequest(BaseModel):
    text: str

# Define API endpoints
@app.get("/")
def read_root():
    return {"message": "AI Text Detector API is running"}

@app.post("/detect")
def detect(request: TextRequest):
    # Check for empty input
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        result = detect_text(model, request.text)
        # Convert label to frontend-expected format
        label = "human" if result["label"] == 0 else "ai"
        return {
            "result": label,              # Matches script.js 'data.result'
            "confidence": float(result["confidence"])  # Matches script.js 'data.confidence'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))