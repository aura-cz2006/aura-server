from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel



class MeetupItem(BaseModel):
    title: str
    date: datetime
    location: dict({'lat': 0.0, 'lng': 0.0})
    id: str
    maxAttendees: int
    rsvpAttendees: list[str]
    