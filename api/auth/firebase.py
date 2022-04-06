import firebase_admin
import os

cred = firebase_admin.credentials.Certificate(
    os.path.join(
        os.getcwd(), 'secrets/serviceAccountKey.json'))
default_app = firebase_admin.initialize_app(cred)

firebase_app = default_app
