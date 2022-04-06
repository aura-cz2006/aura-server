from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, Form
from api.db.models.discussions import update_discussion
from fastapi_cloudauth.firebase import FirebaseClaims
from api.auth.firebase import get_current_user


router = APIRouter()


@router.patch("/{topic}/threads/{thread_id}", summary="", description="", tags=["discussions"])
def patch_discussion_thread(topic: str,
                            thread_id: str,
                            title: Optional[str] = Form(None),
                            content:  Optional[str] = Form(None),
                            current_user: FirebaseClaims = Depends(
                                get_current_user),
                            ):
    # todo: write to db
    discussion = update_discussion(
        thread_id, title, content, topic, datetime.now(), current_user.user_id
    )

    return {"status": "Discussion updated successfully", "updatedDiscussion": discussion}
