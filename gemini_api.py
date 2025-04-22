import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class GoogleChatAPI:
    def __init__(
            self,
            api_key_env = "GEMINI_API_KEY",
            model = "gemini-2.0-flash",
            #max_tokens = 150,
            temperature = 0
    ):
        self.api_key = os.getenv(api_key_env)
        if not self.api_key:
            raise ValueError("Gemini Key not found")
        
        os.environ["GOOGLE_API_KEY"] = self.api_key

        self.model = model
        #self.max_tokens = max_tokens
        self.temperature = temperature

    def start_llm(self):
        llm = ChatGoogleGenerativeAI(
            model = self.model,
            #max_tokens = self.max_tokens,
            temperature = self.temperature
        )

        return llm