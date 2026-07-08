from abc import ABC, abstractmethod
from typing import Dict, Any
from ..schemas.planner import TripContext


class BaseAgent(ABC):
    @abstractmethod
    def execute(self, context: TripContext) -> Dict[str, Any]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass
