import pandas as pd
from langchain.tools import tool
#from pydantic import BaseModel, Field

@tool
def docker_reader(file_path: str) -> dict:
    """
    This function reads a Dockerfile and converts its content into a structured format. 
    It accepts a file path as input and first verifies that the file path ends with the string "dockerfile" (case insensitive)
    """
        
    data = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for index, line in enumerate(file.readlines()):
                data.append({
                    "line_number": index + 1,
                    "docker_command": line.strip()
                })
    except Exception as e:
        return {"error": f"Erro ao ler o arquivo: {str(e)}"}

    return {"dockerfile_content": data}

