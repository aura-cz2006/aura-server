from sys import api_version
from fastapi import APIRouter
import requests

router = APIRouter()


# if __name__=="__main__":
#Authentication parameters
headers = { 'AccountKey': '2Dc6oRWVS6mvNGLiZDfkEQ==',
'accept' : 'application/json'} 

@router.get("/busstops",
summary="Get all bus stop locations",
            description="Gets a list of all bus stops with coords and bus stop code etc from data gov api",
            tags={"buses"})
async def read_busstops():
    api_response = requests.get(
        "http://datamall2.mytransport.sg/ltaodataservice/BusStops",headers=headers)
    if (api_response.status_code == 200):
        return {"busstops": api_response.json()['value']}

    return {}


@router.get("/bustimes/{busstop_id}",
summary="Get all bus times/info of one bus stop",
            description="Gets a list of all bus services with arrival time and type of bus etc from data gov api",
            tags={"buses"})
async def read_bustimes(busstop_id: str):
    api_response = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",headers=headers,params={"BusStopCode":busstop_id})
    if (api_response.status_code == 200):
        return {"bustimes": api_response.json()["Services"]}

    return {}