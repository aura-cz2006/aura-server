from api.main import app
from fastapi.testclient import TestClient
from api.routers import news

###############################
# unit tests

client = TestClient(news.router)


def test_read_news():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == [
        {'id': '1', 'title': 'Nicole promoted to Head Psychologist in IMH'},
        {'id': '2', 'title': 'New cat murderer in Yishun'}
    ]


def test_read_news_item():
    response = client.get('/2')
    assert response.status_code == 200
    assert response.json() == {'id': '2',
                               'title': 'New cat murderer in Yishun'}

##########################
# test router integration


rootClient = TestClient(app)


def test_read_news():
    response = rootClient.get('/news')
    assert response.status_code == 200
    assert response.json() == [
        {'id': '1', 'title': 'Nicole promoted to Head Psychologist in IMH'},
        {'id': '2', 'title': 'New cat murderer in Yishun'}
    ]
