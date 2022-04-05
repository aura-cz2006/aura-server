from datetime import datetime
import json
from typing import Optional
from fastapi import APIRouter, Form


router = APIRouter()




@router.patch("/{meetup_id}", summary="edit a meetup thread", description="edits a meetup thread and updates the db", tags=["meetups"])
def patch_meetup_thread(
    meetup_id: str,
    title: Optional[str] = Form(None),
    description:  Optional[str] = Form(None),
    meetupTime: Optional[str] = Form(None),
    location: Optional[str] = Form(None),
    maxAttendees: Optional[int] = Form(None)
):
    # todo: write to db
    return {"status": "Meetup updated successfully", "createdPost": {
        "id": meetup_id,
        "title": title,
        "description": description,
        "meetupTime": datetime.fromisoformat(meetupTime) if meetupTime else None,
        "location": json.loads(location),
        "maxAttendees": maxAttendees
    }}
