from api.routers.news.get import router
from fastapi.testclient import TestClient


client = TestClient(router)
# (router)


def test_get_news():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {'date': '2022-04-04T00:00:00',
         'id': '1',
         'location': 'Woodlands Ave 6 (Blk 680, 693A)',
         'newstype': 'dengue',
         'numCases': 57},
        {'date': '2022-04-21T00:00:00',
         'eventTitle': 'Cooking class at Bishan CC',
         'fee': 'FREE',
         'id': '2',
         'location': 'Bishan Community Club',
         'newstype': 'ccEvents',
         'url': 'onepa.com'},
        {'date': '2022-04-04T00:00:00',
         'id': '3',
         'location': 'Hougang Street 21',
         'marketName': 'Hougang Wet Market',
         'newstype': 'marketClosure',
         'reopeningDate': '2022-04-16T00:00:00'},
        {'date': '2022-03-04T00:00:00',
         'desc': 'Upgrading of lifts at Aljunied Block 27',
         'endDate': '2022-05-04T00:00:00',
         'id': '4',
         'location': '27 Aljunied Road',
         'newstype': 'upgradingWorks'},
        {'date': '2022-04-01T00:00:00',
         'id': '5',
         'location': 'Ang Mo Kio Ave 10 (Blk 443, 444, 465)',
         'newstype': 'dengue',
         'numCases': 23},
        {'date': '2022-04-03T00:00:00',
         'id': '6',
         'location': 'Woodlands Dr 17',
         'newstype': 'dengue',
         'numCases': 199},
        {'date': '2022-04-06T00:00:00',
         'id': '7',
         'location': 'Admiralty Dr (Blk 353A)',
         'newstype': 'dengue',
         'numCases': 243},
        {'date': '2022-03-04T00:00:00',
         'id': '8',
         'location': "S'goon North Ave 1 ",
         'newstype': 'dengue',
         'numCases': 5},
        {'date': '2022-03-23T00:00:00',
         'id': '9',
         'location': 'Lor 1 Toa Payoh (Blk 174)',
         'newstype': 'dengue',
         'numCases': 83},
        {'date': '2022-04-04T00:00:00',
         'id': '10',
         'location': 'Jln Jurong Kechil / Toh Tuck Rd',
         'newstype': 'dengue',
         'numCases': 234},
    ]


def test_get_single_news_item():
    response = client.get("/2")
    assert response.status_code == 200
    assert response.json() == {
        'date': '2022-04-21T00:00:00',
        'eventTitle': 'Cooking class at Bishan CC',
        'fee': 'FREE',
        'id': '2',
        'location': 'Bishan Community Club',
        'newstype': 'ccEvents',
        'url': 'onepa.com',
    }
