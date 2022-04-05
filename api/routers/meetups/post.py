from datetime import datetime
import json
from fastapi import APIRouter, Form


router = APIRouter()


@router.post("/", summary="post a meetup", description="posts a single meetup item to list of meetups in db", tags=["meetups"])
def post_meetup_thread(
    title: str = Form(...),
    description:  str = Form(...),
    meetupTime: str = Form(...),
    location: str = Form(...),
    maxAttendees: int = Form(...)
):
    # todo: write to db
    id = "9"  # todo: get this from db
    return {"status": "Meetup created successfully", "createdPost": {
        "title": title,
        "description": description,
        "meetupTime": datetime.fromisoformat(meetupTime),
        "location": json.loads(location),
        "id": id,
        "maxAttendees": maxAttendees
    }}
