from typing import Optional
from fastapi import APIRouter, HTTPException

from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_disc_data import sample_disc_data

router = APIRouter()

discussions = sample_disc_data

@router.get("/{topic}/threads", 
            summary="Get all discussion threads of a topic",
            description="Gets all discussions of a certain topic from the db",
            tags=["discussions"])
def read_discussions_threads(topic: str, filter: Optional[str] = ""):
    topiclist = []
    for x in range(len(discussions)):
        if discussions[x].topic == topic:
            topiclist.append(discussions[x])        
    return topiclist

@router.get("/{topic}/threads/{discussion_id}",  
                    summary="Get a discussion item",
                    description="Gets a single discussion item from the db",
                    tags=["discussions"])
def read_discussion_thread(discussion_id: str):
    for x in range(len(discussions)):
        if discussions[x].id == discussion_id:
            return discussions[x]

    raise HTTPException(status_code=404, detail="Discussion Item not found")
