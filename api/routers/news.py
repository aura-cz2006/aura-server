from dataclasses import dataclass
from datetime import datetime
from pydoc_data.topics import topics
from typing import Optional, Sequence
from fastapi import APIRouter

from api.models.news_model import NewsItem
router = APIRouter()

@dataclass
class NewsList:
    news: list[NewsItem]

# dummy news data
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
    ),
    NewsItem(
        id = "3",
        title = "Upgrading of Existing High Covered Linkway",
        # date = datetime()
    ),
    NewsItem(
        id = "4",
        title = "Upgrading of Open Space",
        # date = datetime()
    ),
    NewsItem(
        id = "5",
        title = "Construction of Children`s Playground",
        # date = datetime()
    ),
    NewsItem(
        id = "6",
        title = "Ryan Khong opens a new Japanese restaurant in ION Orchard",
        # ,date = datetime()
    ),
    NewsItem(
        id = "7",
        title = "Alan Seng bakes world's best apple pie",
        # date = datetime()
    ),
    NewsItem(
        id = "8",
        title = "Local University degrees to expire after graduation",
        # date = datetime()
    ),
    NewsItem(
        id = "9",
        title = "Hougang wet market to be closed for upgrading works",
        # date = datetime()
    ),
    NewsItem(
        id = "10",
        title = "New dengue cluster found in Boon Lay",
        # date = datetime()
    )
]


@router.get("/",
            # response_model=NewsList, # <-- breaks docs
            summary="Get news list",
            description="Gets list of all news items from the database",
            tags=["news"])
def read_news(filter: Optional[str] = ""):
    return { "news": news }


@router.get("/{news_id}",
            response_model=NewsItem, 
            summary="Get a news item",
            description="Gets a news item from the database",
            tags=["news"])
def read_news_item(news_id: str):
    for x in range(len(news)):
        if news[x].id == news_id:
            return news[x]
