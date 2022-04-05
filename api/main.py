from fastapi import FastAPI
from .routers.news import get as news_get
from .routers.discussions import get as discussions_get, post as discussions_post, patch as discussions_patch, delete as discussions_delete
from .routers.meetups import get as meetups_get, post as meetups_post, patch as meetups_patch, delete as meetups_delete
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# news
app.include_router(
    news_get.router,
    prefix="/news"
)


# discussions
app.include_router(
    discussions_get.router,
    prefix="/discussions"
)
app.include_router(
    discussions_post.router,
    prefix="/discussions"
)
app.include_router(
    discussions_patch.router,
    prefix="/discussions"
)
app.include_router(
    discussions_delete.router,
    prefix="/discussions"
)

# meetups
app.include_router(
    meetups_get.router,
    prefix="/meetups"
)

app.include_router(
    meetups_post.router,
    prefix="/meetups"
)

app.include_router(
    meetups_patch.router,
    prefix="/meetups"
)

app.include_router(
    meetups_delete.router,
    prefix="/meetups"
)

# static files
app.mount("/static", StaticFiles(directory="api/static"), name="static")


print(__name__)


@ app.get("/", summary="root route", description="used just to test ping the server", tags=["root"])
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
