from fastapi import HTTPException
from api.routers.meetups.patch import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_update_thread():
    response = client.patch("/2", data={
        "title": "new title",
        "description": "new description",
        "location": '{"lat":23.4,"lng":24.4}'
    })
    assert response.status_code == 200
    assert response.json() == {
  "status": "Meetup updated successfully",
  "createdPost": {
    "id": "2",
    "title": "new title",
    "description": "new description",
    "meetupTime": None,
    "location": {
      "lat": 23.4,
      "lng": 24.4
    },
    "maxAttendees": None
  }
}
