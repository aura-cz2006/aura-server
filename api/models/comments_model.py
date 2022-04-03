from dataclasses import dataclass
from datetime import datetime


@dataclass
class CommentItem:
    id: str
    text: str
    user: str
    timestamp: datetime
