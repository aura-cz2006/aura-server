from typing import Optional
from fastapi import APIRouter, HTTPException
from api.models.discussions_model import Topics

# from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_disc_data import sample_disc_data

router = APIRouter()

discussions = sample_disc_data

@router.get("/",
            summary="Get all discussions",
            description="Gets a list of all discussions from the db",
            tags={"discussions"}
            )
def get_news(
):
    return discussions

@router.get("/{topic}/threads", 
            summary="Get all discussion threads of a topic",
            description="Gets all discussions of a certain topic from the db",
            tags=["discussions"])
def read_discussions_threads(topic: str, filter: Optional[str] = ""):

    if not(topic in Topics.__members__):
        raise HTTPException(status_code=404, detail="Topic not found")

    topiclist = []
    for discussion in discussions:
        if discussion.topic == topic:
            topiclist.append(discussion)

    return topiclist


@router.get("/{topic}/threads/{discussion_id}",
            summary="Get a discussion item",
            description="Gets a single discussion item from the db",
            tags=["discussions"])
def read_discussion_thread(discussion_id: str):
    for discussion in discussions:
        if discussion.id == discussion_id:
            return discussion

    raise HTTPException(status_code=404, detail="Thread not found")
