
from datetime import datetime
from api.models.news_model import NewsItem, NewsType


sample_news_data = [
    NewsItem(
        id="1",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04")
    ),
    NewsItem(
        id="2",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="3",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="4",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="5",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="6",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="7",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="8",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="9",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    ),
    NewsItem(
        id="10",
        newstype=NewsType.dengue,
        date=datetime.fromisoformat("2019-12-04"),
    )
]
