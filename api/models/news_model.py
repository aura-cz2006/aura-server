
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
    # reopening for market closure, date for event, end date of upgrading works
    date: Optional[datetime]


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
