
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel

@dataclass
class NewsType(str, Enum):
    Dengue = 'Dengue'
    Marketclosure = 'Market_Closure'
    CCevents = 'CC_Event'
    Upgradingworks = 'Upgrading_works'

class NewsItem(BaseModel):
    id: str
    newstype: NewsType
    date: Optional[datetime]
    
# class DengueNewsItem(NewsItem):
#     numCases: int



# class MarketClosureNewsItem(NewsItem):
    