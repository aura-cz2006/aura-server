from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from api.models.comments_model import CommentItem


class Topics(str, Enum):
    general = 'general'
    nature = 'nature'
    tech = 'tech'
    food = 'food'
    sports = 'sports'


class DiscussionItem(BaseModel):
    id: str
    title: str
    body: str
    topic: Topics
    comments: list[CommentItem]
    date: datetime
