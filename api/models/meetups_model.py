from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

from api.models.comments_model import CommentItem



class MeetupItem(BaseModel):
    title: str
    description: str
    createdAt: datetime
    meetupTime: datetime
    location: dict = ({'lat': 0.0, 'lng': 0.0})
    id: str
    userID: str
    maxAttendees: int
    rsvpAttendees: list[str]
    comments: list[CommentItem]
    isCancelled: bool