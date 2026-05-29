from apify_scraper import scrape_company
from buying_signal import detect_buying_signals

company = scrape_company(
    "https://www.linkedin.com/company/openai"
)[0]

signals = detect_buying_signals(
    company
)

print(signals)