from fastapi import HTTPException
from api.routers.discussions.patch import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_update_thread():
    response = client.patch("/general/threads/2", data={
        "title": "new title",
        "content": "new content"
    })
    assert response.status_code == 200
    assert response.json() == {
  "status": "Discussion updated successfully",
  "updatedPost": {
    "title": "new title",
    "thread_id": "2",
    "content": "new content",
    "topic": "general"
  }
}
