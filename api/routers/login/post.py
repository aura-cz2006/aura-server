import os
import firebase_admin
import firebase_admin.auth as auth


from fastapi import APIRouter, Depends, Header
from api.auth.firebase import get_current_user
from api.db.models.users import upsert_user

from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims


router = APIRouter()


@router.post("/",
             summary="",
             description="",
             tags=["auth"]
             )
def post_login(
    Authorization: str = Header(...),
    current_user: FirebaseClaims = Depends(get_current_user)
):
    print(Authorization)
    id_token = Authorization.split(" ")[1]

    decoded_token = auth.verify_id_token(id_token)

    user = upsert_user(
        uid=decoded_token['sub'],
        display_name=decoded_token['name'],
        email=decoded_token['email'],
        photo_url=decoded_token['picture']
    )

    return {
        "user": user,
        "middleware": current_user
    }
