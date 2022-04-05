from fastapi import APIRouter

router = APIRouter()


@router.delete("/{topic}/threads/{discussion_id}/comments/{comment_id}",
            summary="Creates a comment item",
            description="Adds a comment item to the db",
            tags=["discussions/comments"])
def delete_comment(
    topic: str,
    discussion_id: str,
    comment_id: str
):
    return {
        "status": "Comment deleted successfully",
        "comment_id": comment_id
    }
