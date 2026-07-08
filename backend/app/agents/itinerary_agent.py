from .base_agent import BaseAgent
from ..schemas.planner import TripContext
from ..services.llm import LLMService
from ..prompts.itinerary_prompt import ITINERARY_PROMPT
from ..utils.parser import extract_json
from ..utils.logger import logger


class ItineraryAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMService()

    @property
    def name(self) -> str:
        return "Itinerary"

    def execute(self, context: TripContext) -> dict:
        logger.info(f"{self.name} Agent executing with destination: {context.destination}")
        prompt = ITINERARY_PROMPT.format(
            destination=context.destination, days=context.days or 5
        )
        response = self.llm.generate(prompt)
        return extract_json(response)
