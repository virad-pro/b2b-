from apify_scraper import scrape_company
import json

result = scrape_company(
    "https://www.linkedin.com/company/openai"
)

print(json.dumps(result, indent=4))