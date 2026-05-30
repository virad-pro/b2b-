from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import LinkedInRequest
from apify_scraper import scrape_company
from analyze import analyze_company

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Sales Agent Running"
    }

@app.post("/analyze-company")
def analyze(linkedin: LinkedInRequest):

    companies = scrape_company(
        linkedin.linkedin_url
    )

    company = companies[0]

    return analyze_company(
        company
    )