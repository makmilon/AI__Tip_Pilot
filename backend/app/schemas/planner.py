from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class TripRequest(BaseModel):
    query: str


class DestinationResponse(BaseModel):
    destination: str
    reason: str
    confidence: Optional[float] = None


class ItineraryDay(BaseModel):
    day: int
    activities: List[str]


class ItineraryResponse(BaseModel):
    days: List[ItineraryDay]


class BudgetResponse(BaseModel):
    flight: float
    hotel: float
    food: float
    total: float
    within_budget: bool
    confidence: Optional[str] = None
    reason: Optional[str] = None


class TripContext(BaseModel):
    query: str
    destination: Optional[str] = None
    budget: Optional[float] = None
    days: Optional[int] = None
    interests: Optional[List[str]] = None
    constraints: Optional[List[str]] = None


class PlannerResponse(BaseModel):
    agents_used: List[str]
    destination: Optional[DestinationResponse] = None
    itinerary: Optional[ItineraryResponse] = None
    budget: Optional[BudgetResponse] = None
    warnings: Optional[List[str]] = None
