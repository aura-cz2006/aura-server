import datetime
from peewee import *

from ..db_base_model import DbBaseModel


class DbDiscussion(DbBaseModel):
    id = IntegerField(unique=True, primary_key=True)
    title = CharField(max_length=255)
    content = CharField(max_length=2048)
    topic = CharField(max_length=255)
    date = DateTimeField()
    author_user_id = CharField(max_length=255)

    class Meta:
        db_table = 'discussions'


def get_discussions():
    discussions_query = DbDiscussion.select()
    discussions = []
    for discussion in discussions_query:
        discussions.append(discussion.__data__)
        return discussions


def get_discussion(id: str):
    return DbDiscussion.get(DbDiscussion.id == id).__data__


def create_discussion(
    # id: int,
    title: str, content: str, topic: str, date: datetime, author_user_id: str
):
    discussion_object = DbDiscussion(
        # id=id,
        title=title,
        content=content,
        topic=topic,
        date=date,
        author_user_id=author_user_id
    )
    discussion_object.save()
    return discussion_object.__data__


def update_discussion(
    id: int, title: str, content: str, topic: str, date: datetime, current_user_id: str
):
    query = DbDiscussion.update(
        title=title, content=content, topic=topic, date=date, author_user_id=current_user_id
    ).where(DbDiscussion.id == id, DbDiscussion.author_user_id == current_user_id)
    query.execute()
    discussion = DbDiscussion.get(
        DbDiscussion.id == id)
    return discussion.__data__


def delete_discussion(id: int, current_user_id: str):
    discussion = DbDiscussion.get(
        DbDiscussion.id == id, DbDiscussion.author_user_id == current_user_id)
    deleted_id = discussion.__data__['id']
    discussion.delete_instance()
    return deleted_id
