import uvicorn
from fastapi import FastAPI

from api.routers import discussions
from .routers import news  # ,`` map, community


app = FastAPI()


app.include_router(
    news.router,
    prefix="/news")


app.include_router(
    discussions.router,
    prefix="/discussions")


@app.get("/", summary="root route", description="", tags=["root"])
def read_root():
    return {"isHealthy": True, "caresAboutYou": "❤️", }


# debug
def start_dev():
    """Launched with `poetry run start_dev` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
