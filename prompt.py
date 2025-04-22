import os
from dotenv import load_dotenv
from scrapper_code_tool import docker_reader

load_dotenv()

def prompt():
    file = os.getenv("PATH_CODE")
    CODE_URL = os.getenv("URL_CODE_DOCS")
    REPO_URL = os.getenv("URL_REPO_DOCS")
    CODE = docker_reader.invoke(file)

    query = f"""
        You are a formal code reviewer. Use your tools to verify that the submitted code is well-written, free of errors, 
        and does not contain sensitive data. Additionally, analyze the project's repository documentation to ensure that 
        the code will not cause performance issues or downtime when deployed to production. 
        Verify that the written code meets all project requirements by cross-referencing the documentation in the repository:

        Review it, following this steps :
        1. Code best pratices in {CODE_URL}
        2. Project documentation in {REPO_URL}

        If, at the end of the analysis, the code is not aligned with or relevant to the project's objectives as outlined in the documentation, 
        make sure to emphasize this in the final response. The same applies if the code contains insecure information or is poorly written. 
        In either case, do not recommend its deployment

        Code:
        {CODE}
    """

    return query.strip()