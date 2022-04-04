from fastapi import APIRouter, Form


router = APIRouter()


@router.delete("/{topic}/threads/{thread_id}", summary="", description="", tags=["discussions"])
def delete_discussion_thread(topic: str,
                             thread_id: str):
    # todo: handle db delete query
    return {"status": "Discussion deleted successfully", "updatedPost": {
        "topic": topic,
        "thread_id": thread_id,
    }}
