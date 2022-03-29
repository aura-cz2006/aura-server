# from typing import Optional
# from fastapi import APIRouter

# from api.models.discussions_model import DiscussionItem, Topics

# router = APIRouter()


# discussions = [
#     DiscussionItem(
#         id="1",
#         topic=Topics.General,
#         title="Where is the cleanest toilet in Singapore?",
#         # date=datetime()
#     ),
#     DiscussionItem(
#         id="2",
#         topic=Topics.General,
#         title="Best barber in the East?",
#         # date = datetime()
#     ),
#     DiscussionItem(
#         id="3",
#         topic=Topics.Nature,
#         title="New exhibit in Punggol Park in Singapore",
#         # date = datetime()
#     )
# ]


# @router.get("/{topic}/threads", tags=["discussions"])
# def read_discussions_threads(topic: str, filter: Optional[str] = ""):
#     return discussions


# @router.get("/{topic}/threads/{discussion_id}", tags=["discussions"])
# def read_discussion_thread(discussion_id: str):
#     for x in range(len(discussions)):
#         if discussions[x].id == discussion_id:
#             return discussions[x]
