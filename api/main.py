from urllib import response
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
import firebase_admin.auth as auth

from .auth import firebase
from .db.database import conn as db_conn
from .routers.login import post as login_post
from .routers.news import get as news_get
from .routers.discussions import get as discussions_get, post as discussions_post, patch as discussions_patch, delete as discussions_delete
from .routers.discussions.comments import post as discussions_comments_post, delete as discussions_comments_delete
from .routers.meetups import get as meetups_get, post as meetups_post, patch as meetups_patch, delete as meetups_delete
from .routers.meetups.comments import post as meetups_comments_post, delete as meetups_comments_delete
from fastapi.staticfiles import StaticFiles


app = FastAPI()


@app.on_event("startup")
async def startup():
    firebase_app = firebase.firebase_app  # init firebase
    if db_conn.is_closed():
        db_conn.connect()


@app.on_event("shutdown")
async def shutdown():
    print("Closing...")
    if not db_conn.is_closed():
        db_conn.close()


@app.middleware("http")
async def add_firebase_auth_middleware(request: Request, call_next):

    response = await call_next(request)
    try:

        authentication_header_value = request.headers.get("authorization")
        id_token = authentication_header_value.split(" ")[1]

        print(id_token)

        path = request.url.path
        print(path)

        return response

    except:
        return JSONResponse(status_code=401, content=jsonable_encoder({"error": "You are not authorized"}))


# news
app.include_router(
    login_post.router,
    prefix="/login"
)

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
