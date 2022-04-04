
from datetime import datetime
from api.models.news_model import CCEventNewsItem, DengueNewsItem, MarketClosureNewsItem, NewsItem, NewsType, UpgradingNewsItem


sample_news_data = [
    DengueNewsItem(
        id="1",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {'lat':1.2644,
        'lng':103.8222},
        numCases= 69,
    ),
    CCEventNewsItem(
        id="2",
        newstype=NewsType.ccEvents,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        eventTitle= "Jamie's birthday party",
        url= "instagram.com",
        fee= "FREE!!!",
    ),
    MarketClosureNewsItem(
        id="3",
        newstype=NewsType.marketClosure,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        marketName= "Hougang Wet Market",
        reopeningDate= datetime.fromisoformat("2019-12-16"),
    ),
    UpgradingNewsItem(
        id="4",
        newstype=NewsType.upgradingWorks,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        desc= "Upgrading of lifts at Aljunied Block 27",
        endDate= datetime.fromisoformat("2019-12-27"),
    ),
    DengueNewsItem(
        id="5",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        numCases= 69,
    ),
    DengueNewsItem(
        id="6",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        numCases= 69,
    ),
    DengueNewsItem(
        id="7",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        numCases= 69,
    ),
    DengueNewsItem(
        id="8",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        numCases= 69,
    ),
    DengueNewsItem(
        id="9",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        location= {"lat":1.2644,
        "lng":103.8222},
        numCases= 69,
    ),
    DengueNewsItem(
        id="10",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
        
        numCases= 69,
    )
]
