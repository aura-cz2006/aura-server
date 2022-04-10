from fastapi import HTTPException
from api.routers.meetups.get import router
from fastapi.testclient import TestClient
from pytest import raises


client = TestClient(router)


def test_get_meetups():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "title": "Badminton game @ bishan",
            "description": "Is anyone up for a game of badminton? For beginners!",
            "createdAt": "2020-06-04T00:00:00",
            "meetupTime": "2022-06-04T00:00:00",
            "location": {
                "lat": 1.3526,
                "lng": 103.8352
            },
            "id": "1",
            "userID": "1",
            "maxAttendees": 15,
            "rsvpAttendees": [
                "1",
                "2",
                "3"
            ],
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
            "isCancelled": False
        },
        {
            "title": "Friendly neighbourhood get together",
            "description": "Anybody in their 20s interested to be friends?",
            "createdAt": "2020-06-04T00:00:00",
            "meetupTime": "2022-06-04T00:00:00",
            "location": {
                "lat": 1.3526,
                "lng": 103.8352
            },
            "id": "2",
            "userID": "3",
            "maxAttendees": 8,
            "rsvpAttendees": [
                "2",
                "3",
                "4"
            ],
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
            "isCancelled": False
        },
        {
            "title": "Steamboat for CNY",
            "description": "Opening my house to anyone!",
            "createdAt": "2020-06-04T00:00:00",
            "meetupTime": "2022-06-04T00:00:00",
            "location": {
                "lat": 1.3526,
                "lng": 103.8352
            },
            "id": "3",
            "userID": "3",
            "maxAttendees": 5,
            "rsvpAttendees": [
                "3",
                "4",
                "5"
            ],
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
            "isCancelled": False
        },
        {
            "title": "Looking for skating buddies",
            "description": "Recently picked up skating!",
            "createdAt": "2020-06-04T00:00:00",
            "meetupTime": "2022-06-04T00:00:00",
            "location": {
                "lat": 1.3526,
                "lng": 103.8352
            },
            "id": "4",
            "userID": "4",
            "maxAttendees": 8,
            "rsvpAttendees": [
                "2",
                "3",
                "4"
            ],
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
            "isCancelled": False
        }
    ]


def test_get_single_meetup_item():
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() == {
        'comments': [{'id': '1',
                      'text': 'Fantastico!',
                      'timestamp': '2019-12-04T00:00:00',
                      'user': '1'},
                     {'id': '2',
                      'text': 'This is such a good thread!',
                      'timestamp': '2019-12-04T00:00:00',
                      'user': '2'},
                     {'id': '3',
                      'text': '=D',
                      'timestamp': '2019-12-04T00:00:00',
                      'user': '3'},
                     {'id': '4',
                      'text': 'Wow I didnt know this =p thanks for sharing',
                      'timestamp': '2019-12-04T00:00:00',
                      'user': '4'},
                     {'id': '5',
                      'text': 'Coooooool beans!',
                      'timestamp': '2019-12-04T00:00:00',
                      'user': '5'}],
        'createdAt': '2020-06-04T00:00:00',
        'description': 'Anybody in their 20s interested to be friends?',
        'id': '2',
        'isCancelled': False,
        'location': {'lat': 1.2643,
                     'lng': 103.82231},
        'maxAttendees': 8,
        'meetupTime': '2022-06-04T00:00:00',
        'rsvpAttendees': ['2',
                          '3',
                          '4'],
        'title': 'Friendly neighbourhood get together',
        'userID': '3',
    }


def test_get_single_meetup_item_nonexistent():
    with raises(HTTPException) as err:
        client.get("/12")
    assert err.value.status_code == 404
    assert err.value.detail == "Thread not found"
