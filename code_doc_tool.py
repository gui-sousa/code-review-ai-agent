from scrapper_url_tool import get_text_url
from langchain.tools import tool
#from pydantic import BaseModel, Field

@tool
def code_documentation(url: str) -> dict:
    """
    This tool receives a URL containing Docker documentation on best practices for Dockerfile creation and 
    provides optimized recommendations for writing secure, efficient, and well-structured Dockerfiles.
    """
    code_response = get_text_url(url)
    
    return {"code_documentation": code_response}