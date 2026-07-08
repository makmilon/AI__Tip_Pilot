from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import planner, history

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TripPilot AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(planner.router)
app.include_router(history.router)


@app.get("/")
async def root():
    return {"message": "TripPilot AI Backend"}
