from fastapi.testclient import TestClient


from ..routers import news


client = TestClient(news.router)


def test_read_news():
    response = client.get('/news')
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
