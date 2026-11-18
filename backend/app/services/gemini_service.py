from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from app.core.config import settings


class GeminiService:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.LLM_MODEL,
            api_key=settings.GEMINI_API_KEY,
            max_retries=1,
            timeout=60
        )

    def generate(self, prompt: str) -> str:
        response = self.llm.invoke([
            HumanMessage(content=prompt)
        ])

        return response.text


gemini_service = GeminiService()