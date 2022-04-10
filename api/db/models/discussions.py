import datetime
from peewee import *
import firebase_admin.auth as auth

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


def add_discussion_data(discussion):
    user_id = discussion['author_user_id']
    print(user_id)
    user = auth.get_user(user_id)
    print(user.display_name)

    discussion = dict(discussion)

    discussion.__delitem__("author_user_id")
    discussion.__setitem__("author", {
        "id": user_id,
        "displayName": user.display_name
    })

    discussion.__setitem__("liked_by", [])

    from .discussion_comments import get_comments_of_single_discussion
    comments = get_comments_of_single_discussion(discussion['id'])
    discussion.__setitem__("comments", comments)

    return discussion


def get_discussions():
    query = DbDiscussion.select()
    print(f"length of query return: {len(query)}")
    discussions = []
    for discussion in query:
        data = add_discussion_data(discussion.__data__)
        discussions.append(data)

    return discussions


def get_discussion(id: str):
    discussion = DbDiscussion.get(DbDiscussion.id == id).__data__
    data = add_discussion_data(discussion.__data__)
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
