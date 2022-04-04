from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel



class MeetupItem(BaseModel):
    title: str
    date: datetime
    location: dict({'Lat': '0', 'Long': '0'})
    id: str
    maxAttendees: int
    rsvpAttendees: list[str]
    