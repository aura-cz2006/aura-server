from typing import Optional
from fastapi import APIRouter, Form


router = APIRouter()


@router.patch("/{topic}/threads/{thread_id}", summary="", description="", tags=["discussions"])
def patch_discussion_thread(topic: str,
                            thread_id: str,
                            title: Optional[str] = Form(...),
                            content:  Optional[str] = Form(...),
                            ):
    # todo: write to db
    return {"status": "Discussion updated successfully", "updatedPost": {
        "title": title,
        "thread_id": thread_id,
        "content": content,
        "topic": topic
    }}
