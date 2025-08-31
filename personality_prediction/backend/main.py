from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from typing import List

app = FastAPI(title="ATS Analyzer API")

# ✅ Root route
@app.get("/")
def read_root():
    return { "Backend is running!"}

# ✅ CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Pydantic response model
class ATSResponse(BaseModel):
    score: int
    missing_keywords: List[str]
    suggestions: List[str]
    strengths: List[str]

# ✅ Main route
@app.post("/analyze", response_model=ATSResponse)
async def analyze_cv(file: UploadFile = File(...)):
    missing_keywords = [
        "Machine Learning",
        "Data Analysis",
        
    ]
    suggestions = [
          "Highlight hands-on experience with cloud platforms .",
           "List any certifications."
           "Mention modern tools"
        
    ]
    strengths = [
        "Strong foundation in problem-solving and algorithms.",
        "Good use of technical buzzwords relevant to the job role.",
        "Well-structured CV with clear section hierarchy.",
    ]
    score = random.randint(70, 85)
    return ATSResponse(
        score=score,
        missing_keywords=missing_keywords,
        suggestions=suggestions,
        strengths=strengths,
    )