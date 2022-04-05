from datetime import datetime
from fastapi import APIRouter, Form, HTTPException

router = APIRouter()


@router.post("/{meetup_id}/comments",
             summary="Creates a comment item",
             description="Adds a comment item to the db",
             tags=["meetups/comments"])
def create_meetup_comment(
    meetup_id: str,
    text: str = Form(...)
):
    # check if meetup with meetup_id exists
    return {
        "status": "Comment added successfully",
        "meetup_id": meetup_id,
        "text": text,
        "timestamp": datetime.now(),
        "user": "todo"
    }
