from fastapi import HTTPException
from api.routers.discussions.post import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_create_comment():
    response = client.post("/general/threads/2/comments", data={
        "text": "woah, thanks for informing me fellow citizen. Xie Xie"
    })
