from typing import Optional
from fastapi import APIRouter, HTTPException

# from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_meetup_data import sample_meetup_data

router = APIRouter()

meetups = sample_meetup_data


@router.get("/",
            summary="Get all meetups",
            description="Gets all meetups from the db",
            tags=["meetups"])
def read_meetup_threads():
    return meetups


@router.get("/{meetup_id}",
            summary="Get a meetup item",
            description="Gets a single meetup item from the db",
            tags=["meetups"])
def read_meetup_thread(meetup_id: str):
    for meetup_item in meetups:
        if meetup_item.id == meetup_id:
            return meetup_item

    raise HTTPException(status_code=404, detail="Thread not found")
