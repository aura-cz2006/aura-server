from api.fixtures.news_fixtures import news_fixtures
from api.main import app
from fastapi.testclient import TestClient
from api.routers import news

###############################
# unit tests

client = TestClient(news.router)


def test_read_news(news_fixtures):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == news_fixtures


def test_read_news_item(news_fixtures):
    response = client.get('/2')
    assert response.status_code == 200
    assert response.json() == news_fixtures[1]

##########################
# test router integration


rootClient = TestClient(app)


def test_root_read_news(news_fixtures):

    response = rootClient.get('/news')
    assert response.status_code == 200
    assert response.json() == news_fixtures
