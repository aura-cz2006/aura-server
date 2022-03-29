from typing import Optional
from fastapi import APIRouter

from api.models.discussions_model import DiscussionItem, Topics

router = APIRouter()


discussions = [
    DiscussionItem(
        id="1",
        topic=Topics.General,
        title="Nicole promoted to Head Psychologist in IMH",
        # date=datetime()
    ),
    DiscussionItem(
        id="2",
        topic=Topics.General,
        title="New cat murderer in Yishun",
        # date = datetime()
    )
]


@router.get("/{topic}/threads", tags=["discussions"])
def read_discussions_threads(topic: str, filter: Optional[str] = ""):
    return discussions


@router.get("/{topic}/threads/{discussion_id}", tags=["discussions"])
def read_discussion_thread(discussion_id: str):
    for x in range(len(discussions)):
        if discussions[x].id == discussion_id:
            return discussions[x]
