
from dataclasses import dataclass
from enum import Enum

@dataclass
class NewsType(Enum):
    Dengue = 1
    Marketclosure = 2
    CCevents = 3
    Upgradingworks = 4
@dataclass
class NewsItem:
    id: str
    title: str
    newstype: NewsType
    # date: Optional[datetime]
    
    