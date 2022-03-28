from dataclasses import dataclass
import enum
from typing import Optional, Sequence
from fastapi import APIRouter

router = APIRouter()


@dataclass
class DiscussionItem:
    id: str
    topic: enum(Nature = "Nature",General = "General") #this is not working
    title: str


discussions = [
    DiscussionItem(
        id= "1",
        topic = "Nature",
        title= "Nicole promoted to Head Psychologist in IMH",
        # date=datetime()
    ),
    DiscussionItem(
        id = "2",
        topic = "General",
        title = "New cat murderer in Yishun",
        # date = datetime()
    )

    # {"id": "1", "title": "Nicole promoted to Head Psychologist in IMH"},
    # {"id": "2", "title": "New cat murderer in Yishun"}
]


@router.get("/", tags=["news"])
async def read_discussions(filter: Optional[str] = ""):

    return discussions


@router.get("/{news_id}", tags=["news"])
async def read_news_item(news_id: str):
    for x in range(len(news)):
        if news[x].id == news_id:
            return news[x]
