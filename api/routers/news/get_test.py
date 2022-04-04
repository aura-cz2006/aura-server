from api.routers.news.get import router
from fastapi.testclient import TestClient


client = TestClient(router)
# (router)


def test_get_news():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
    {
        "id": "1",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "2",
        "newstype": "ccEvents",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "eventTitle": "Jamie's birthday party",
        "url": "instagram.com",
        "fee": "FREE!!!"
    },
    {
        "id": "3",
        "newstype": "marketClosure",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "marketName": "Hougang Wet Market",
        "reopeningDate": "2019-12-16T00:00:00"
    },
    {
        "id": "4",
        "newstype": "upgradingWorks",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "desc": "Upgrading of lifts at Aljunied Block 27",
        "endDate": "2019-12-27T00:00:00"
    },
    {
        "id": "5",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "6",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "7",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "8",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "9",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "numCases": 69
    },
    {
        "id": "10",
        "newstype": "dengue",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 0.0,
            "lng": 0.0
        },
        "numCases": 69
    }
]


def test_get_single_news_item():
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() ==  {
        "id": "2",
        "newstype": "ccEvents",
        "date": "2019-12-04T00:00:00",
        "location": {
            "lat": 1.2644,
            "lng": 103.8222
        },
        "eventTitle": "Jamie's birthday party",
        "url": "instagram.com",
        "fee": "FREE!!!"
    }