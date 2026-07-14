from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Career AI API",
    description="Backend API for the Career AI platform.",
    version="0.1.0",
)

app.include_router(api_router)