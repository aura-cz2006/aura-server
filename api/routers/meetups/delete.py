from fastapi import APIRouter, Form


router = APIRouter()


@router.delete("/{meetup_id}", summary="Delete a meetup", description="Sets isCancelled=True", tags=["meetups"])
def delete_meetup_thread(
        meetup_id: str):
    # todo: handle db delete query
    return {"status": "Meetup deleted successfully", "updatedPost": {
        "id": meetup_id,
        "isCancelled": True
    }}
