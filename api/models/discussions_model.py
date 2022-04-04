from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from api.models.comments_model import CommentItem


class Topics(str, Enum):
    General = 'General'
    Nature = 'Nature'
    Tech = 'Tech'
    Food = 'Food'
    Sports = 'Sports'


class DiscussionItem(BaseModel):
    id: str
    title: str
    topic: Topics
    comments: list[CommentItem]
    date: datetime
