from code_doc_tool import code_documentation
from repo_doc_tool import repo_documentation
from scrapper_code_tool import docker_reader
from prompt import prompt
from gemini_api import GoogleChatAPI
from langchain.agents import initialize_agent, AgentType


llm = GoogleChatAPI().start_llm()
tools = [docker_reader, code_documentation, repo_documentation]


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = prompt()

if __name__ == "__main__":
    response = agent.invoke({"input": query})
    print(response['output'])