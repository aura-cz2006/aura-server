from fastapi import APIRouter, Form


router = APIRouter()


@router.post("/{topic}/threads", summary="", description="", tags=["discussions"])
def post_discussion_thread(topic: str,
                           title: str = Form(...),
                           content:  str = Form(...),
                           ):
    # todo: write to db
    id = "9"  # todo: get this from db
    return {"status": "Discussion created successfully", "createdPost": {
        "title": title,
        "id": id,
        "content": content,
        "topic": topic
    }}
