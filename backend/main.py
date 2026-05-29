from fastapi import FastAPI
from scraper import scrape_website

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Sales Agent Running"
    }


@app.get("/scrape")
def scrape(url: str):
    return scrape_website(url)