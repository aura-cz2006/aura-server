from typing import Union
from charset_normalizer import detect
from fastapi import APIRouter, HTTPException

from api.models.news_model import CCEventNewsItem, DengueNewsItem, MarketClosureNewsItem, UpgradingNewsItem
from api.sample.sample_news_data import sample_news_data


router = APIRouter()


# todo: integrate db here
# for now we're using sample data
news_data = sample_news_data
print(news_data)


@router.get("/",
            # response_model=list[news_item_response_model],
            summary="Get news items",
            description="Gets a list of news from the db",
            tags={"news"}
            )
def get_news(
):
    return news_data


@router.get("/{news_id}",
            # response_model=news_item_response_model,
            summary="Get a news item",
            description="Gets a single news item from the db",
            tags={"news"}
            )
def get_single_news(news_id: str):
    for news_item in news_data:
        if news_item.id == news_id:
            return news_item

    raise HTTPException(status_code=404, detail="News Item not found")
