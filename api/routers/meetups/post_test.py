from datetime import datetime
import json
from fastapi import HTTPException
from api.models.meetups_model import MeetupItem
from api.routers.meetups.post import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_create_meetup():
    response = client.post("/", data={
        "title": "some title",
        "description": "some description",
        "meetupTime": "2022-03-03",
        "location": '{"lat": 27.3, "lng": 55.5}',
        "maxAttendees": 27
    })
    assert response.status_code == 200
    assert response.json() == {
        "status": "Meetup created successfully",
        "createdPost": {
            "title": "some title",
            "description": "some description",
            "meetupTime": "2022-03-03T00:00:00",
            "location": {
                "lat": 27.3,
                "lng": 55.5
            },
            "id": "9",
            "maxAttendees": 27
        }
    }
