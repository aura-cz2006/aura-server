from datetime import datetime
from fastapi import APIRouter, Form, HTTPException

router = APIRouter()


@router.get("/{topic}/threads/{discussion_id}/comments",
            summary="Creates a comment item",
            description="Adds a comment item to the db",
            tags=["discussions/comments"])
def create_comment(topic: str,
                 discussion_id: str,
                 text: str = Form(...)
                 ):
    # check if discussion with discussion_id exists
    return {
        "status": "Comment added successfully", "topic": topic,
        "discussion_id": discussion_id,
        "text": text,
        "timestamp": datetime.now(),
        "user": "todo"
    }
