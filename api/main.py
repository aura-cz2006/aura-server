import uvicorn
from fastapi import FastAPI


from .routers import news


app = FastAPI()


app.include_router(
    news.router,
    prefix="/news")


# app.include_router(
#     discussions.router,
#     prefix="/discussions")

print(__name__)


@app.get("/", summary="root route", description="", tags=["root"])
def read_root():
    return {"isHealthy": True, "caresAboutYou": "❤️", }


# debug
def start_dev():
    """Launched with `poetry run start_dev` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)


def start_prod():
    uvicorn.run("api.main:app",
                host="0.0.0.0",
                port=8000,
                ssl_keyfile="../ssl/key.pem",
                ssl_certfile="../ssl/cert.pem",
                reload=False
                )
