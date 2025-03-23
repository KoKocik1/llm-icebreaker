from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import load_dotenv
from output_parsers import Summary, TopicOfInterest, IceBreakers
from typing import Tuple
from tools.tools import get_profile_photo_url
from chains.custom_chains import get_summary_chain, get_interests_chain, get_ice_breaker_chain


def ice_breaker(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    linkedin_picture_url = get_profile_photo_url(linkedin_data)

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data},
    )

    interests_chain = get_interests_chain()
    interests: TopicOfInterest = interests_chain.invoke(
        input={"information": linkedin_data}
    )

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers: IceBreakers = ice_breaker_chain.invoke(
        input={"information": linkedin_data}
    )

    return (
        summary_and_facts,
        interests,
        ice_breakers,
        linkedin_picture_url,
    )

    # return (summary_and_facts, linkedin_picture_url)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker(
        name="Krzysztof Kokot Software Developer at Statscore Świętochłowice")
