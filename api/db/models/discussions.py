import datetime
from peewee import *

from ..db_base_model import DbBaseModel
from .users import DbUser


class DbDiscussion(DbBaseModel):
    id = IntegerField(unique=True, primary_key=True)
    title = CharField(max_length=255)
    content = CharField(max_length=2048)
    topic = CharField(max_length=255)
    date = DateTimeField()
    author_user_id = ForeignKeyField(DbUser)

    class Meta:
        db_table = 'discussions'


def get_discussions():
    query = DbDiscussion.select()
    print(f"length of query return: {len(query)}")
    discussions = []
    for discussion in query:
        data = discussion.__data__
        data.__setitem__("liked_by", [])

        from .discussion_comments import get_comments_of_single_discussion
        comments = get_comments_of_single_discussion(discussion.id)
        data.__setitem__("comments", comments)
        discussions.append(discussion.__data__)

    return discussions


def get_discussion(id: str):
    data = DbDiscussion.get(DbDiscussion.id == id).__data__
    user_id = data['author_user_id']
    print(user_id)
    user = DbUser.get(DbUser.uid == user_id).__data__
    print(user)
    data.__setitem__("liked_by", [])
    data.__setitem__("comments_by", [])
    return data


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
