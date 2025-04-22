from scrapper_url_tool import get_text_url
from langchain.tools import tool
#from pydantic import BaseModel, Field

@tool
def repo_documentation(url: str) -> dict:
    """
    This tool receives the repository URL and analyzes the provided documentation to extract 
    detailed information about the project's functionality and dependencies.
    """

    repo_response = get_text_url(url)
    
    return {"repo_documentation": repo_response}