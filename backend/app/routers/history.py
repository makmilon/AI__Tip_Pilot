from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..repositories.request_repository import RequestRepository
from ..models.request_log import RequestLog

router = APIRouter(prefix="/api", tags=["history"])

@router.get("/history")
async def get_history(db: Session = Depends(get_db)):
    repository = RequestRepository(db)
    logs = repository.get_all_logs()
    return [
        {
            "id": log.id,
            "query": log.query,
            "agents_used": log.agents_used,
            "destination": log.destination,
            "created_at": log.created_at,
        }
        for log in logs
    ]

@router.delete("/history")
async def clear_history(db: Session = Depends(get_db)):
    repository = RequestRepository(db)
    repository.delete_all_logs()
    return {"message": "History cleared successfully"}
