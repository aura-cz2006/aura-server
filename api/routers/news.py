from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Sequence
from fastapi import APIRouter

router = APIRouter()


@dataclass
class NewsItem:
    id: str
    title: str
    # date: Optional[datetime]


news = [
    NewsItem(
        id= "1",
        title= "Nicole promoted to Head Psychologist in IMH",
        # date=datetime()
    ),
    NewsItem(
        id = "2",
        title = "New cat murderer in Yishun",
        # date = datetime()
    )
]


@router.get("/", 
            summary="Gets news items",
            description="You can provide a filter via query param",
            tags=["news"])
def read_news(filter: Optional[str] = ""):

    return news


@router.get("/{news_id}",
            response_model=NewsItem, 
            summary="Get a news item",
            description="Gets a news item from the database",
            tags=["news"])
def read_news_item(news_id: str):
    for x in range(len(news)):
        if news[x].id == news_id:
            return news[x]
