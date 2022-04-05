from fastapi import HTTPException
from api.routers.meetups.comments.delete import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_delete_meetup_comment():
    response = client.delete("/2/comments/5")
    assert response.status_code == 200
    assert response.json() == {'comment_id': '5',
                               'status': 'Comment deleted successfully'}
