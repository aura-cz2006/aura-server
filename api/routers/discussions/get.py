from typing import Optional
from fastapi import APIRouter, HTTPException
from api.models.discussions_model import Topics
from api.db.models.discussions import get_discussions, get_discussion


# from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_disc_data import sample_disc_data

router = APIRouter()


@router.get("/",
            summary="Get all discussions",
            description="Gets a list of all discussions from the db",
            tags={"discussions"}
            )
def get_news(
):
    return get_discussions()


# @router.get("/{topic}/threads",
#             summary="Get all discussion threads of a topic",
#             description="Gets all discussions of a certain topic from the db",
#             tags=["discussions"])
# def read_discussions_threads(topic: str, filter: Optional[str] = ""):

#     if not(topic in Topics.__members__):
#         raise HTTPException(status_code=404, detail="Topic not found")

#     # topiclist = []
#     # for discussion in :
#     #     if discussion.topic == topic:
#     #         topiclist.append(discussion)

#     return get_discussion()


@router.get("/{topic}/threads/{discussion_id}",
            summary="Get a discussion item",
            description="Gets a single discussion item from the db",
            tags=["discussions"])
def read_discussion_thread(discussion_id: str):
    return get_discussion(discussion_id)
