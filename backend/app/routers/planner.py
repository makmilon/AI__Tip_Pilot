from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.planner import TripRequest, PlannerResponse
from ..services.orchestrator import Orchestrator
from ..repositories.request_repository import RequestRepository
from ..utils.logger import logger
from ..config import settings
import traceback

router = APIRouter(prefix="/api", tags=["planner"])


@router.get("/test")
async def test_api():
    return {
        "gemini_key_set": len(settings.GEMINI_API_KEY) > 0,
        "message": "API test endpoint working"
    }


@router.post("/planner", response_model=PlannerResponse)
async def generate_plan(request: TripRequest, db: Session = Depends(get_db)):
    try:
        logger.info(f"Received request: {request.query}")
        if len(settings.GEMINI_API_KEY) == 0:
            raise Exception("GEMINI_API_KEY is not set")
        orchestrator = Orchestrator()
        response = orchestrator.execute(request.query)
        repository = RequestRepository(db)
        repository.create_log(request, response)
        return response
    except Exception as e:
        logger.error(f"Error in generate_plan: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
