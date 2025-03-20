from langchain_community.tools.tavily_search import TavilySearchResults
import json


def get_profile_url_tavily(name: str) -> str:
    """Search the web to find a LinkedIn profile URL"""
    search = TavilySearchResults()
    result = search.run(f"{name}")
    return result


def get_profile_photo_url(linkedin_data: str) -> str:
    picture_url = linkedin_data.get("photo_url")
    if not picture_url:
        picture_url = "https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg"
    return picture_url
