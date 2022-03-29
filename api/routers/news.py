from dataclasses import dataclass
from datetime import datetime
from pydoc_data.topics import topics
from typing import Optional, Sequence
from fastapi import APIRouter

from api.models.news_model import NewsItem, NewsType
router = APIRouter()

@dataclass
class NewsList:
    news: list[NewsItem]

# dummy news data
news = [
    NewsItem(
        id= "1",
        title= "Nicole promoted to Head Psychologist in IMH",
        newstype= NewsType.CCevents
        # date=datetime()
    ),
    NewsItem(
        id = "2",
        title = "New cat murderer in Yishun",
        newstype= NewsType.CCevents
        # date = datetime()
    ),
    NewsItem(
        id = "3",
        title = "Upgrading of Existing High Covered Linkway",
        newstype= NewsType.Upgradingworks
        # date = datetime()
    ),
    NewsItem(
        id = "4",
        title = "Upgrading of Open Space",
        newstype= NewsType.Upgradingworks
        # date = datetime()
    ),
    NewsItem(
        id = "5",
        title = "Construction of Children`s Playground",
        newstype= NewsType.Upgradingworks
        # date = datetime()
    ),
    NewsItem(
        id = "6",
        title = "Ryan Khong opens a new Japanese restaurant in ION Orchard",
        newstype= NewsType.CCevents
        # ,date = datetime()
    ),
    NewsItem(
        id = "7",
        title = "Alan Seng bakes world's best apple pie",
        newstype= NewsType.CCevents
        # date = datetime()
    ),
    NewsItem(
        id = "8",
        title = "Local University degrees to expire after graduation",
        newstype= NewsType.CCevents
        # date = datetime()
    ),
    NewsItem(
        id = "9",
        title = "Hougang wet market to be closed for upgrading works",
        newstype= NewsType.Marketclosure
        # date = datetime()
    ),
    NewsItem(
        id = "10",
        title = "New dengue cluster found in Boon Lay",
        newstype= NewsType.Dengue
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
            #response_model=NewsItem, #  <-- this is breaking shit suddenly too 
            summary="Get a news item",
            description="Gets a news item from the database",
            tags=["news"])
def read_news_item(news_id: str):
    for x in range(len(news)):
        if news[x].id == news_id:
            return news[x]
