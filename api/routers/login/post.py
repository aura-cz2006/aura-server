import firebase_admin.auth as auth


from fastapi import APIRouter, Header
from api.auth.firebase import firebase_app
from api.db.models.users import create_user


router = APIRouter()


@router.post("/",
             summary="",
             description="",
             tags=["auth"]
             )
def post_login(
    Authorization: str = Header(...)
):
    # print(Authorization)
    id_token = Authorization.split(" ")[1]

    decoded_token = auth.verify_id_token(id_token)

    user = create_user(
        uid=decoded_token['user_id'],
        display_name=decoded_token['name'], email=decoded_token['email'],
        photo_url=decoded_token['picture']
    )

    return {
        # "decoded_token": decoded_token['picture'],
        "user": user
    }
