"""
NWVIT Resume Tool API
Author: Aaron Barkley
Version: 0.1.0
Date: April 14, 2025

This is the main FastAPI application for the NWVIT Resume Compatibility Tool.
"""


# Import 
from fastapi import FastAPI
from pydantic import BaseModel

#Create and instance of FastAPI - this will serve as our main app
app = FastAPI()

#Define what is expected in the POST request
class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str

#Define a GET route at the root URL ('/')
#When someone accesses http://localhost:8000/, this function is triggered
@app.get("/")
def read_root():
    return {"message": "NWVIT Resume Tool API is live!"}

@app.post("/analyze")
def analyze_resume(request: ResumeAnalysisRequest):
    #Placeholder: In the future, add real parsing & scoring here
    fake_score = 87
    feedback = "Consider adding more keywords from the job description."

    return {
        "score": fake_score,
        "feedback": feedback
    }


