from fastapi import HTTPException
from api.routers.discussions.post import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_create_thread():
    response = client.post("/general/threads", data={
        "title": "some title",
        "content": "some content"
    })
    assert response.status_code == 200
    assert response.json() == {
        'createdPost': {'content': 'some content',
                        'id': '9',
                        'title': 'some title',
                        'topic': 'general'},
        'status': 'Discussion created successfully',
    }
