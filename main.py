"""
NWVIT Resume Tool API
Author: Aaron Barkley
Version: 0.1.0
Date: April 14, 2025

This is the main FastAPI application for the NWVIT Resume Compatibility Tool.
"""
# Reminder: Activate virtual environment before running!

#### AARON DO THIS FIRST DUMMY ####

# Windows PowerShell:cd "C:\Users\aaron\OneDrive\Desktop\NWVIT\ats-project" 
# .\venv\Scripts\Activate.ps1
# Server reset :uvicorn main:app --reload

# Test Location
# http://127.0.0.1:8000/docs

# Imports 
from fastapi import FastAPI
from pydantic import BaseModel
import re
import string

from fastapi.middleware.cors import CORSMiddleware


# Utility Functions
def clean_text(text):
    # Normalize common smart/Word characters
    text = text.replace('\r', ' ').replace('\n', ' ')
    text = text.replace('“', '"').replace('”', '"').replace("’", "'")
    text = text.replace('\t', ' ')
    text = text.replace("•", " ")   # common Word bullet
    text = text.replace("", " ")   # Word's weird bullet dot
    text = text.replace("–", "-")   # en dash
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)  # Collapse extra spaces
    return text.strip()

#Create and instance of FastAPI - this will serve as our main app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In development, allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    resume_cleaned = clean_text(request.resume_text)
    job_desc_cleaned = clean_text(request.job_description)
    score, missing = analyze_match(resume_cleaned, job_desc_cleaned)

    return {
        "score": score,
        "missing_keywords": missing,
        "feedback": f"You're missing {len(missing)} important keywords from the job description"
    }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Resume Analysis Logic
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def analyze_match(resume_text, job_desc_text):
    #phrase based keywords to extract from job description
    target_keywords = {
        "cybersecurity": {"network security", "infosec", "information security", "cyber security"},
        "siem": {"splunk", "log management"},
        "threat detection": {"incident response", "threat hunting", "bug bounty"},
        "python": {"python3", "py"},
        "fastapi": {"api development"},
        "analyst": {"engineer", "specialist", "technician", "security lead"},
    }

    #clean up punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    resume_clean = resume_text.lower().translate(translator)
    job_desc_text = job_desc_text.lower().translate(translator)

    #check each keyword and its synonyms
    matched = set()
    for keyword, synonyms in target_keywords.items():
        if keyword in resume_clean or any(syn in resume_clean for syn in synonyms):
            matched.add(keyword)

    total_keywords = set(target_keywords.keys())
    missing_keywords = total_keywords - matched
    score = (len(matched)/len(total_keywords)) * 100 if total_keywords else 0

    #return the results
    return round(score, 2), sorted(list(missing_keywords))
