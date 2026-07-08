from .base_agent import BaseAgent
from ..schemas.planner import TripContext
from ..services.llm import LLMService
from ..prompts.destination_prompt import DESTINATION_PROMPT
from ..utils.parser import extract_json
from ..utils.logger import logger


class DestinationAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMService()

    @property
    def name(self) -> str:
        return "Destination"

    def execute(self, context: TripContext) -> dict:
        logger.info(f"{self.name} Agent executing with query: {context.query}")
        prompt = DESTINATION_PROMPT.format(query=context.query)
        response = self.llm.generate(prompt)
        return extract_json(response)
