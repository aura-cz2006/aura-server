from api.routers.discussions.get import router
from fastapi.testclient import TestClient


client = TestClient(router)
# (router)


def test_get_threads():
    response = client.get("/general/threads")
    assert response.status_code == 200
    assert response.json() == [
    {
        "id": "1",
        "title": "Where is the cleanest toilet in Singapore?",
        "topic": "general",
        "comments": [
            {
                "id": "1",
                "text": "Fantastico!",
                "user": "1",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "2",
                "text": "This is such a good thread!",
                "user": "2",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "3",
                "text": "=D",
                "user": "3",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "4",
                "text": "Wow I didnt know this =p thanks for sharing",
                "user": "4",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "5",
                "text": "Coooooool beans!",
                "user": "5",
                "timestamp": "2019-12-04T00:00:00"
            }
        ],
        "date": "2019-12-04T00:00:00"
    },
    {
        "id": "2",
        "title": "Best barber in the East?",
        "topic": "general",
        "comments": [
            {
                "id": "1",
                "text": "Fantastico!",
                "user": "1",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "2",
                "text": "This is such a good thread!",
                "user": "2",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "3",
                "text": "=D",
                "user": "3",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "4",
                "text": "Wow I didnt know this =p thanks for sharing",
                "user": "4",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "5",
                "text": "Coooooool beans!",
                "user": "5",
                "timestamp": "2019-12-04T00:00:00"
            }
        ],
        "date": "2019-12-04T00:00:00"
    }
]

def test_get_single_disc_item():
    response = client.get("/general/threads/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": "2",
        "title": "Best barber in the East?",
        "topic": "general",
        "comments": [
            {
                "id": "1",
                "text": "Fantastico!",
                "user": "1",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "2",
                "text": "This is such a good thread!",
                "user": "2",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "3",
                "text": "=D",
                "user": "3",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "4",
                "text": "Wow I didnt know this =p thanks for sharing",
                "user": "4",
                "timestamp": "2019-12-04T00:00:00"
            },
            {
                "id": "5",
                "text": "Coooooool beans!",
                "user": "5",
                "timestamp": "2019-12-04T00:00:00"
            }
        ],
        "date": "2019-12-04T00:00:00"
    }
