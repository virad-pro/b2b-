from fastapi import FastAPI

from models import LinkedInRequest
from apify_scraper import scrape_company
from analyze import analyze_company

app = FastAPI()


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