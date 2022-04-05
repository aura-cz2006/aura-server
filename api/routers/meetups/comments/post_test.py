from fastapi import HTTPException
from .post import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_create_meetup_comment():
    response = client.post("/2/comments", data={
        "text": "woah, thanks for informing me fellow citizen. Xie Xie"
    })
    assert response.status_code == 200
    # assert response.json() == {}
