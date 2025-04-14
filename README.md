# NWVIT Resume Compatibility Tool

**An open-source tool that helps veterans compare their resumes against job descriptions to get real-time feedback and a compatibility score.**

---

## Created for:

![NWVIT Logo](Logo.png)


## Project Purpose

Veterans often struggle with translating their military experience into civilian terms. This tool aims to reduce that barrier by analyzing resume and job description content to provide actionable feedback — helping our members become more competitive job seekers.

---

## Current Features

- ✅ FastAPI backend running locally
- ✅ `/analyze` endpoint accepts resume + job description
- ✅ Returns a sample compatibility score and basic feedback
- ✅ Auto-generated API docs with Swagger (`/docs`)

---

## Tech Stack

- FastAPI
- Uvicorn
- Python 3.13
- Markdown, Git, and GitHub

---

## How to Run Locally

1. Clone the repo:
   git clone https://github.com/lumberjack3E/nwvit-ats.git
   cd nwvit-ats

2. Create a virtual environment:
   py -m venv venv

3. Activate Enviorment (Windows)
   .\venv\Scripts\Activate.ps1

4. Install Dependencies
   pip install fastapi uvicorn

5. Run the Server
   uvicorn main:app --reload

6. Visit
   http://127.0.0.1:8000/docs

## Roadmap
-[ ] Add real resume scoring
-[ ] Support file uploads
-[ ] Expand keyword feedback
-[ ] Add simple frontend

## License
MIT — use it, modify it, contribute to it. Just keep the original author credited.

## Author
Created by [Aaron Barkley (Lumberjack 3 Echo)](https://github.com/lumberjack3E)  
VP, [NWVIT](https://www.nwvit.org)

