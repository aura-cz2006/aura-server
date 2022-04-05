from fastapi import HTTPException
from api.routers.discussions.get import router
from fastapi.testclient import TestClient
from pytest import raises


client = TestClient(router)


def test_get_all_threads():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "1",
            "title": "Where is the cleanest toilet in Singapore?",
            "content": "Some content for the discussion",
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
            "date": "2019-12-04T00:00:00",
            "userID": "1",
            "likedBy": [
                "1",
                "2",
                "3"
            ]
        },
        {
            "id": "2",
            "title": "Best barber in the East?",
            "content": "Some content for the discussion",
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
            "date": "2019-12-04T00:00:00",
            "userID": "2",
            "likedBy": [
                "1",
                "2",
                "3"
            ]
        },
        {
            "id": "3",
            "title": "New exhibit in Punggol Park in Singapore",
            "content": "Some content for the discussion",
            "topic": "nature",
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
            "date": "2019-12-04T00:00:00",
            "userID": "3",
            "likedBy": [
                "1",
                "2",
                "3"
            ]
        }
    ]


def test_get_threads():
    response = client.get("/general/threads")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "1",
            "title": "Where is the cleanest toilet in Singapore?",
            "content": "Some content for the discussion",
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
            "date": "2019-12-04T00:00:00",
            "userID": "1",
            "likedBy": [
                "1",
                "2",
                "3"
            ]
        },
        {
            "id": "2",
            "title": "Best barber in the East?",
            "content": "Some content for the discussion",
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
            "date": "2019-12-04T00:00:00",
            "userID": "2",
            "likedBy": [
                "1",
                "2",
                "3"
            ]
        }
    ]


def test_get_threads_unexpected_topic():
    with raises(HTTPException) as err:
        client.get("/anime/threads")
    assert err.value.status_code == 404
    assert err.value.detail == "Topic not found"


def test_get_single_disc_item():
    response = client.get("/general/threads/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": "2",
        "title": "Best barber in the East?",
        "content": "Some content for the discussion",
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
        "date": "2019-12-04T00:00:00",
        "userID": "2",
        "likedBy": [
            "1",
            "2",
            "3"
        ]
    }


def test_get_single_disc_item_nonexistent():
    with raises(HTTPException) as err:
        client.get("/general/threads/12")
    assert err.value.status_code == 404
    assert err.value.detail == "Thread not found"
