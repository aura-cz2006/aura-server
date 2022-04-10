from sys import api_version
from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/market_closure",
            summary="Get market closure dates",
            tags={"market-closure"}
            )
async def read_market_closure():
    api_response = requests.get(
        "https://data.gov.sg/api/action/datastore_search?resource_id=b80cb643-a732-480d-86b5-e03957bc82aa"
    )

    if (api_response.status_code == 200):
        data = api_response.json()['result']['records']
        for item in data:
            del item['longitude_hc']
            del item['latitude_hc']
        return {"market_closures": data}

    return {}
