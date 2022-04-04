
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NewsType(str, Enum):
    dengue = 'dengue'
    marketClosure = 'marketClosure'
    ccEvents = 'ccEvents'
    upgradingWorks = 'upgradingWorks'


class NewsItem(BaseModel):
    id: str
    newstype: NewsType
    date: Optional[datetime]
    location: dict = ({'lat': 0.0, 'lng': 0.0})


class DengueNewsItem(NewsItem):
    numCases: int


class MarketClosureNewsItem(NewsItem):
    marketName: str
    reopeningDate: datetime


class CCEventNewsItem(NewsItem):
    eventTitle: str
    url: str
    fee: str


class UpgradingNewsItem(NewsItem):
    desc: str
    endDate: datetime
