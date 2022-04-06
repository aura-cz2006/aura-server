

from typing import Optional
from fastapi import APIRouter, Header


router = APIRouter()


@router.post("/",
             #  docs
             )
def post_login(
    bearer_token: str = Header(...)
):
    print(bearer_token)
    return {bearer_token}
