from apify_scraper import scrape_company
from niche_detector import detect_niche

company = scrape_company(
    "https://www.linkedin.com/company/openai"
)[0]

result = detect_niche(company)

print(result)