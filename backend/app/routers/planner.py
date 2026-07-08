from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.planner import TripRequest, PlannerResponse
from ..services.orchestrator import Orchestrator
from ..repositories.request_repository import RequestRepository

router = APIRouter(prefix="/api", tags=["planner"])


@router.post("/planner", response_model=PlannerResponse)
async def generate_plan(request: TripRequest, db: Session = Depends(get_db)):
    orchestrator = Orchestrator()
    response = orchestrator.execute(request.query)
    repository = RequestRepository(db)
    repository.create_log(request, response)
    return response
