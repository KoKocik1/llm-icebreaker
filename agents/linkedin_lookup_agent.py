from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain import hub
from tools.tools import get_profile_url_tavily
from tools.mongo import get_mongo_client
from config.config import COLLECTION_LINKS
from config.config import DB_NAME

load_dotenv()


def lookup(name: str) -> str:

    client = get_mongo_client()
    db = client[DB_NAME]
    collection = db[COLLECTION_LINKS]

    cached_profile = collection.find_one({"name": name})

    if cached_profile:
        # If the LinkedIn URL is already cached in the database, return it
        print(f"Using cached LinkedIn URL for {name}")
        return cached_profile["linkedin_url"]

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"],
        template=template,
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 3 linkedin profile page",
            description="useful when you need to get the LinkedIn url of a person",
            func=get_profile_url_tavily,
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]

    if linked_profile_url.endswith("/en"):
        linked_profile_url = linked_profile_url[:-3]

    collection.insert_one({"name": name, "linkedin_url": linked_profile_url})
    return linked_profile_url


if __name__ == "__main__":
    print(lookup("Eden Marco"))
