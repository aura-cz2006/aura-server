from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers.news import get as news_get
from .routers.discussions import get as discussions_get, post as discussions_post, patch as discussions_patch, delete as discussions_delete
from .routers.discussions.comments import post as discussions_comments_post, delete as discussions_comments_delete
from .routers.meetups import get as meetups_get, post as meetups_post, patch as meetups_patch, delete as meetups_delete
from .routers.meetups.comments import post as meetups_comments_post, delete as meetups_comments_delete
from .routers.proxy import taxis as proxy_taxis, buses as proxy_buses, amenities as proxy_amenities

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
app.include_router(
    discussions_comments_post.router,
    prefix="/discussions"
)
app.include_router(
    discussions_comments_delete.router,
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
app.include_router(
    meetups_comments_post.router,
    prefix="/discussions"
)
app.include_router(
    meetups_comments_delete.router,
    prefix="/discussions"
)

# proxy
app.include_router(
    proxy_taxis.router,
    prefix="/proxy/taxis"
)

app.include_router(
    proxy_buses.router,
    prefix="/proxy/buses"
)

app.include_router(
    proxy_amenities.router,
    prefix="/proxy/amenities"
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
