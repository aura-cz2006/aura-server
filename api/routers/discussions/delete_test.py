from fastapi import HTTPException
from api.routers.discussions.delete import router
from fastapi.testclient import TestClient
from pytest import raises

client = TestClient(router)


def test_delete_thread():
    response = client.delete("/general/threads/2")
    assert response.status_code == 200
    assert response.json() == {
        # 'status': 'Discussion deleted successfully',
        # 'updatedPost': {'thread_id': '2',
        #                 'topic': 'general'},

    }
