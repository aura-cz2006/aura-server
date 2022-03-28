from api.main import app
from fastapi.testclient import TestClient
from api.models.discussions import DiscussionItem, Topics
from api.routers import discussions

############
# unit tests

client = TestClient(discussions.router)


def test_read_discussions():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == [
    DiscussionItem(
        id= "1",
        topic = Topics.General,
        title= "Nicole promoted to Head Psychologist in IMH",
        # date=datetime()
    ),
    DiscussionItem(
        id = "2",
        topic = Topics.General,
        title = "New cat murderer in Yishun",
        # date = datetime()
    )
]


def test_read_discussion_item():
    response = client.get('/2')
    assert response.status_code == 200
    assert response.json() == {'id': '2',
                               'title': 'New cat murderer in Yishun'}


#########################
# test router integration