from .get import router
from fastapi.testclient import TestClient


client = TestClient(router)
(router)


def test_get_news():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {'date': '2019-12-04T00:00:00',
         'id': '1',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '2',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '3',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '4',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '5',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '6',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '7',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '8',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '9',
         'newstype': 'dengue'},
        {'date': '2019-12-04T00:00:00',
         'id': '10',
         'newstype': 'dengue'},
    ]


def test_get_single_news_item():
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() == {
        'date': '2019-12-04T00:00:00', 'id': '2', 'newstype': 'dengue'}
