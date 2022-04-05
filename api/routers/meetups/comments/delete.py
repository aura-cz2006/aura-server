from fastapi import APIRouter

router = APIRouter()


@router.delete("/{meetup_id}/comments/{comment_id}",
            summary="Creates a comment item",
            description="Adds a comment item to the db",
            tags=["meetups/comments"])
def delete__meetup_comment(
    meetup_id: str,
    comment_id: str
):
    return {
        "status": "Comment deleted successfully",
        "comment_id": comment_id
    }
