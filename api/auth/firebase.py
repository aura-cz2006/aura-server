import firebase_admin
import os

from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims

creds_path = os.path.join(
    os.getcwd(), 'secrets/serviceAccountKey.json')

cred = firebase_admin.credentials.Certificate(
    creds_path)

default_app = firebase_admin.initialize_app(cred)

firebase_app = default_app

get_current_user = FirebaseCurrentUser(
    project_id=firebase_admin.get_app().project_id,
)
