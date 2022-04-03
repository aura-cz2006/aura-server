from dataclasses import dataclass
from enum import Enum

from api.models.comments_model import CommentItem


@dataclass
class Topics(Enum):
    General = 'General'
    Nature = 'Nature'
    Tech = 'Tech'
    Food = 'Food'
    Sports = 'Sports'


@dataclass
class DiscussionItem:
    id: str
    title: str
    topic: Topics
    comments: list[CommentItem]
