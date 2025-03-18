import requests


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from a LinkedIn profile,
    Manually scrape the information from the LinkedIn profile
    """
    response = None

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/KoKocik1/43cf61bd36f577a2f95ed61b5b154c4c/raw/4db1ebff52d96f1631aa2678ac5188cc9ff92984/gistfile1.txt"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        ).json()
    else:
        # call external API
        response = "No implementation yet"

    response = {k: v for k, v in response.items() if v != None and v != ""}
    return response


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            "https://www.linkedin.com/in/guido-van-luijk-9354b25", mock=True
        )
    )
