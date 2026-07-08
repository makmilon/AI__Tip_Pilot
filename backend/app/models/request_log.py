from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from ..database import Base


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(Text, nullable=False)
    destination = Column(JSON, nullable=True)
    itinerary = Column(JSON, nullable=True)
    budget = Column(JSON, nullable=True)
    agents_used = Column(JSON, nullable=True)
    final_response = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
