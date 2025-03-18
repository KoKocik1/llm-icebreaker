from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello, World!")
    # print(os.environ['OPEN_API_KEY'])

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. a list of 2-3 interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    llm = ChatOllama(model="gemma:2b")

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile("", mock=True)

    res = chain.invoke({"information": linkedin_data})

    print(res)
