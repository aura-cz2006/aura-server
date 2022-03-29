import uvicorn
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from api.routers import discussions
from .routers import news  # ,`` map, community


app = FastAPI()


app.include_router(
    news.router,
    prefix="/news")


# app.include_router(
#     discussions.router,
#     prefix="/discussions")


@app.get("/", summary="root route", description="", tags=["root"])
def read_root():
    return {"isHealthy": True, "caresAboutYou": "❤️", }


# debug
def start_dev():
    """Launched with `poetry run start_dev` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)


def start_prod():
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["aura-app.xyz", "*.aura-app.xyz"]
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    uvicorn.run("api.main:app",
                host="0.0.0.0",
                port=8000,
                ssl_keyfile="../ssl/key.pem",
                ssl_certfile="../ssl/cert.pem",
                reload=False
                )
