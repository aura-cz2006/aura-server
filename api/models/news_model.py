
from dataclasses import dataclass


@dataclass
class NewsItem:
    id: str
    title: str
    # date: Optional[datetime]