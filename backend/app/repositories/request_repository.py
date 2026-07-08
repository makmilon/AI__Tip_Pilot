from sqlalchemy.orm import Session
from ..models.request_log import RequestLog
from ..schemas.planner import PlannerResponse, TripRequest

class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_log(
        self, request: TripRequest, response: PlannerResponse
    ) -> RequestLog:
        db_log = RequestLog(
            query=request.query,
            destination=response.destination.model_dump() if response.destination else None,
            itinerary=response.itinerary.model_dump() if response.itinerary else None,
            budget=response.budget.model_dump() if response.budget else None,
            agents_used=response.agents_used,
            final_response=response.model_dump(),
        )
        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)
        return db_log

    def get_all_logs(self) -> list[RequestLog]:
        return self.db.query(RequestLog).order_by(RequestLog.created_at.desc()).all()

    def delete_all_logs(self) -> None:
        self.db.query(RequestLog).delete()
        self.db.commit()
