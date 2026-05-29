import os

from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

client = ApifyClient(
    os.getenv("APIFY_API_TOKEN")
)


def scrape_company(linkedin_url):

    run_input = {
        "companies": [
            linkedin_url
        ]
    }

    run = client.actor(
        "harvestapi/linkedin-company"
    ).call(
        run_input=run_input
    )
    print(run)
    print(type(run))

    dataset_id = run.default_dataset_id

    items = list(
        client.dataset(dataset_id).iterate_items()
    )

    return items