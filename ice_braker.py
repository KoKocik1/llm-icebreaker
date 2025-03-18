from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import load_dotenv


def ice_breaker(name: str):
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. a list of 2-3 interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # llm = ChatOllama(model="gemma:2b")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke({"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker(name="Krzysztof Kokot Software Developer at Statscore Świętochłowice")
