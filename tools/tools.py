from langchain_community.tools.tavily_search import TavilySearchResults
import json


def get_profile_url_tavily(name: str) -> str:
    """Search the web to find a LinkedIn profile URL"""
    search = TavilySearchResults()
    result = search.run(f"{name}")
    return result
