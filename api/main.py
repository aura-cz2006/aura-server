import uvicorn
from fastapi import FastAPI
from .routers.news import get as news_get
from .routers.discussions import get as discussions_get


app = FastAPI()

# news
app.include_router(
    news_get.router,
    prefix="/news"
)
# discussions
app.include_router(
    discussions_get.router,
    prefix="/news"
)

print(__name__)


@app.get("/", summary="root route", description="used just to test ping the server", tags=["root"])
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
