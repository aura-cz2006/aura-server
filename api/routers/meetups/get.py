from typing import Optional
from fastapi import APIRouter, HTTPException

from api.models.discussions_model import MeetupItem, Topics
from api.sample.sample_disc_data import sample_disc_data

router = APIRouter()

discussions = sample_disc_data


@router.get("/{topic}/threads", 
            summary="Get all discussion threads",
            description="Gets all discussions from the db",
            tags=["discussions"])
def read_discussions_threads(topic: str, filter: Optional[str] = ""):
    return discussions


@router.get("/{topic}/threads/{discussion_id}",  
                    summary="Get a discussion item",
                    description="Gets a single discussion item from the db",
                    tags=["discussions"])
def read_discussion_thread(discussion_id: str):
    for x in range(len(discussions)):
        if discussions[x].id == discussion_id:
            return discussions[x]

    raise HTTPException(status_code=404, detail="Discussion Item not found")
