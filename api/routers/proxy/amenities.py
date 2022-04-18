from sys import api_version
from fastapi import APIRouter
import requests

router = APIRouter()
#token is expired should change to post req
# @router.post("/"),
# def read_new_token():
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjg2NzEsInVzZXJfaWQiOjg2NzEsImVtYWlsIjoia2tob25nMDAxQGUubnR1LmVkdS5zZyIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTY0OTIzMTk2NSwiZXhwIjoxNjQ5NjYzOTY1LCJuYmYiOjE2NDkyMzE5NjUsImp0aSI6ImI3NDJmZDNjNDEzNGVjMTBmMGNiMGIzMzI4NjE5OTJlIn0.HePZ8JaoPOsvHRIL3eZ78Doths1WOE3yuAI6vGShaXA'

@router.get("/{query}",
summary="Get all specified amenity locations",
            description="Gets a list of specified amenity locations from onemap api, first entry is definition of specified amenity",
            tags={"amenities"})
async def read_amenities(query: str):
    api_response = requests.get("https://developers.onemap.sg/privateapi/themesvc/retrieveTheme",params={"token":token,"queryName":query})
    if (api_response.status_code == 200):
        return {"query": api_response.json()["SrchResults"]}

    return {}