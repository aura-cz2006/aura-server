from sys import api_version
from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/",
            summary="Get all taxi locations",
            description="Gets a list of all taxi coordinates from data gov api",
            tags={"taxis"})
async def read_taxis():
    api_response = requests.get(
        "https://api.data.gov.sg/v1/transport/taxi-availability")
    if (api_response.status_code == 200):
        return {"taxis": api_response.json()['features'][0]['geometry']['coordinates']}

    return {}
