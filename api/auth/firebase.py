import firebase_admin
import os

from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims


cred = firebase_admin.credentials.Certificate(
    os.path.join(
        os.getcwd(), 'secrets/serviceAccountKey.json'))
default_app = firebase_admin.initialize_app(cred)

firebase_app = default_app

get_current_user = FirebaseCurrentUser(
    project_id=firebase_admin.get_app().project_id,
)
