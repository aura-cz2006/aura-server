from fastapi import HTTPException
from api.routers.meetups.delete import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_delete_thread():
    response = client.delete("/2")
    assert response.status_code == 200
    assert response.json() == {
        "status": "Meetup deleted successfully",
        "updatedPost": {
            "id": "2",
            "isCancelled": True
        }
    }
