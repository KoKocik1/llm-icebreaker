from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import load_dotenv
from output_parser import summary_parser, Summary
from typing import Tuple
from tools.tools import get_profile_photo_url


def ice_breaker(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_template = """
        Given the information about a person from linkedin {information} I want you to create:
        1. a short summary
        2. a list of 2-3 interesting facts about them
        \n\n
        {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # llm = ChatOllama(model="gemma:2b")

    chain = summary_prompt_template | llm | summary_parser

    picture_url = get_profile_photo_url(linkedin_data)

    summary_and_facts: Summary = chain.invoke({"information": linkedin_data})

    return (summary_and_facts, picture_url)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker(name="Krzysztof Kokot Software Developer at Statscore Świętochłowice")
