from fastapi import HTTPException
from api.routers.discussions.post import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_create_thread():
    response = client.post("/general/threads", data={
        "title": "some title",
        "body": "some body"
    })
    assert response.status_code == 200
    assert response.json() == {
        'createdPost': {'body': 'some body',
                        'thread_id': '9',
                        'title': 'some title',
                        'topic': 'general'},
        'status': 'Discussion created successfully',
    }
