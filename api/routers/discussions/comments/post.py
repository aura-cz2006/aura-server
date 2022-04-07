from datetime import datetime
from fastapi import APIRouter, Form, Depends
from fastapi_cloudauth.firebase import FirebaseClaims
from api.auth.firebase import get_current_user

from api.db.models.discussion_comments import add_comment_to_discussion

router = APIRouter()


@router.post("/{topic}/threads/{discussion_id}/comments",
             summary="Creates a comment item",
             description="Adds a comment item to the db",
             tags=["discussions/comments"])
def create_comment(
    # topic: str,
    discussion_id: str,
    text: str = Form(...),
    current_user: FirebaseClaims = Depends(get_current_user),
):
    # check if discussion with discussion_id exists

    new_comment = add_comment_to_discussion(
        current_user_id=current_user.user_id,
        discussion_id=discussion_id,
        content=text
    )

    return {
        "status": "Comment added successfully",
        "createdComment": new_comment
        # "topic": topic,
        # "discussion_id": discussion_id,
        # "text": text,
        # "timestamp": datetime.now(),
        # "user": "todo"
    }
