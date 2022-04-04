# from api.main import app
# from fastapi.testclient import TestClient
# from api.models.discussions_model import DiscussionItem, Topics
# from api.routers import discussions

# ############
# # unit tests

# client = TestClient(discussions.router)


# def test_read_discussions():
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.json() == [
#     DiscussionItem(
#         id= "1",
#         topic = Topics.General,
#         title= "Where is the cleanest toilet in Singapore?",
#         # date=datetime()
#     ),
#     DiscussionItem(
#         id = "2",
#         topic = Topics.General,
#         title = "Best barber in the East?",
#         # date = datetime()
#     )
# ]


# def test_read_discussion_item():
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.json() == {'id': '2',
#                             'title': 'Best barber in the East?'}


# #########################
# # test router integration

# rootClient = TestClient(app)

# def test_read_discussions():
#     response = rootClient.get('/')
#     assert response.status_code == 200
#     assert response.json() == [
#     DiscussionItem(
#         id= "1",
#         topic = Topics.General,
#         title= "Where is the cleanest toilet in Singapore?",
#         # date=datetime()
#     ),
#     DiscussionItem(
#         id = "2",
#         topic = Topics.General,
#         title = "Best barber in the East?",
#         # date = datetime()
#     )
# ]