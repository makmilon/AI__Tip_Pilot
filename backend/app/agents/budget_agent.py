from .base_agent import BaseAgent
from ..schemas.planner import TripContext
from ..services.llm import LLMService
from ..prompts.budget_prompt import BUDGET_PROMPT
from ..utils.parser import extract_json
from ..utils.logger import logger


class BudgetAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMService()

    @property
    def name(self) -> str:
        return "Budget"

    def execute(self, context: TripContext) -> dict:
        logger.info(f"{self.name} Agent executing with destination: {context.destination}")
        prompt = BUDGET_PROMPT.format(
            destination=context.destination, query=context.query
        )
        response = self.llm.generate(prompt)
        return extract_json(response)
