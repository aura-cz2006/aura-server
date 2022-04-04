from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel



class CommentItem(BaseModel):
    id: str
    text: str
    user: str
    timestamp: datetime
