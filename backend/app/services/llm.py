import google.generativeai as genai
from ..config import settings
from ..utils.logger import logger

logger.info(f"GEMINI_API_KEY is set? {len(settings.GEMINI_API_KEY) > 0}")
genai.configure(api_key=settings.GEMINI_API_KEY)


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"Generating content with prompt length: {len(prompt)}")
            response = self.model.generate_content(prompt)
            logger.info(f"LLM response received")
            return response.text
        except Exception as e:
            logger.error(f"LLM generation error: {e}")
            import traceback
            logger.error(traceback.format_exc())
            raise
