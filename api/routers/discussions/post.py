from datetime import datetime
from fastapi import APIRouter, Depends, Form
from fastapi_cloudauth.firebase import FirebaseClaims
from api.auth.firebase import get_current_user
from api.db.models.discussions import create_discussion


router = APIRouter()


@router.post("/{topic}/threads", summary="", description="", tags=["discussions"])
def post_discussion_thread(
    topic: str,
    title: str = Form(...),
    content:  str = Form(...),
    current_user: FirebaseClaims = Depends(get_current_user),
):
    discussion = create_discussion(
        title, content, topic, datetime.now(), current_user.user_id
    )

    id = "9"  # todo: get this from db
    return {"status": "Discussion created successfully", "createdDiscussion": discussion}
