from fastapi import APIRouter, Depends, Form
from fastapi_cloudauth.firebase import FirebaseClaims
from api.auth.firebase import get_current_user
from api.db.models.discussions import delete_discussion

router = APIRouter()


@router.delete("/{topic}/threads/{thread_id}", summary="", description="", tags=["discussions"])
def delete_discussion_thread(topic: str,
                             thread_id: str,
                             current_user: FirebaseClaims = Depends(
                                 get_current_user),
                             ):

    deletedDiscussionId = delete_discussion(thread_id, current_user.user_id)

    return {"status": "Discussion deleted successfully", "deletedId": deletedDiscussionId}
