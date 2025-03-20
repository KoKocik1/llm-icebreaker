from selenium import webdriver
import requests
import os
from dotenv import load_dotenv
from linkedin_scraper import Person, actions
import json
from tools.mongo import get_mongo_client
from config.config import COLLECTION_PROFILES
from config.config import DB_NAME

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from a LinkedIn profile,
    Manually scrape the information from the LinkedIn profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/KoKocik1/43cf61bd36f577a2f95ed61b5b154c4c/raw/4db1ebff52d96f1631aa2678ac5188cc9ff92984/gistfile1.txt"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        ).json()
        response = {k: v for k, v in response.items() if v != None and v != ""}
    else:
        client = get_mongo_client()
        db = client[DB_NAME]
        collection = db[COLLECTION_PROFILES]
        cached_data = collection.find_one(
            {"linkedin_url": linkedin_profile_url})
        if cached_data:
            print(f"Using cached data for {linkedin_profile_url}")
            response = cached_data.get("response")

        else:
            driver = webdriver.Chrome()

            email = os.getenv("LINKEDIN_EMAIL")
            password = os.getenv("LINKEDIN_PASSWORD")

            actions.login(driver, email, password)
            response = Person(linkedin_profile_url,
                              driver=driver).person_to_json()

            response = {
                k: v
                for k, v in response.items()
                if v not in ([], "", "", None) and k not in ["certifications"]
            }

            collection.insert_one(
                {"response": response, "linkedin_url": linkedin_profile_url}
            )

    return response


if __name__ == "__main__":
    print(scrape_linkedin_profile(
        "https://www.linkedin.com/in/krzysztof-kokot-dev/"))
