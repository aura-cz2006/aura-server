from peewee import *

from ..db_base_model import DbBaseModel


class DbUser(DbBaseModel):
    uid = CharField(max_length=255, unique=True, primary_key=True)
    display_name = CharField(max_length=255)
    email = CharField(max_length=255)
    photo_url = CharField(max_length=255)

    class Meta:
        db_table = 'users'


def upsert_user(uid: str, display_name: str, email: str, photo_url: str):
    user_object = DbUser(
        uid=uid,
        display_name=display_name,
        email=email,
        photo_url=photo_url,
    )
    try:
        user_object.save(force_insert=True)
    except:
        user_object.replace()
    return user_object.__data__


def get_user(uid: str):
    return DbUser.filter(DbUser.uid == uid).first()
