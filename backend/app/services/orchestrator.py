import re
from typing import List, Dict, Any, Optional
from ..schemas.planner import TripContext, PlannerResponse
from ..agents.base_agent import BaseAgent
from ..agents.destination_agent import DestinationAgent
from ..agents.itinerary_agent import ItineraryAgent
from ..agents.budget_agent import BudgetAgent
from ..utils.logger import logger


class Orchestrator:
    def __init__(self):
        self.destination_agent = DestinationAgent()
        self.itinerary_agent = ItineraryAgent()
        self.budget_agent = BudgetAgent()

    def parse_query(self, query: str) -> TripContext:
        days_match = re.search(r"(\d+)\s*(day|days)", query, re.IGNORECASE)
        days = int(days_match.group(1)) if days_match else None

        budget_match = re.search(r"[£$€](\d+)", query)
        budget = float(budget_match.group(1)) if budget_match else None

        return TripContext(
            query=query,
            days=days,
            budget=budget,
        )

    def execute(self, query: str) -> PlannerResponse:
        logger.info(f"Orchestrator received query: {query}")
        context = self.parse_query(query)

        agents_used: List[str] = []
        destination: Optional[Dict] = None
        itinerary: Optional[Dict] = None
        budget: Optional[Dict] = None

        destination = self.destination_agent.execute(context)
        agents_used.append(self.destination_agent.name)
        context.destination = destination.get("destination")

        itinerary = self.itinerary_agent.execute(context)
        agents_used.append(self.itinerary_agent.name)

        budget = self.budget_agent.execute(context)
        agents_used.append(self.budget_agent.name)

        return PlannerResponse(
            agents_used=agents_used,
            destination=destination,
            itinerary=itinerary,
            budget=budget,
        )
