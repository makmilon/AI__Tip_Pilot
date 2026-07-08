import google.generativeai as genai
from ..config import settings
from ..utils.logger import logger

genai.configure(api_key=settings.GEMINI_API_KEY)


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"LLM generation error: {e}")
            raise
