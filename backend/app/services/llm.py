import google.genai as genai
from ..config import settings
from ..utils.logger import logger

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMService:
    def __init__(self):
        pass

    def generate(self, prompt: str) -> str:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"LLM generation error: {e}")
            raise
