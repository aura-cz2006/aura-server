import datetime
from peewee import *
from datetime import datetime

from api.db.db_base_model import DbBaseModel
from .users import DbUser
from .discussions import DbDiscussion


class DbDiscussionComment(DbBaseModel):
    comment_id = IntegerField(primary_key=True)
    discussion_id = ForeignKeyField(DbDiscussion)
    timestamp = DateTimeField()
    author_user_id = ForeignKeyField(DbUser)
    content = CharField(max_length=255)

    class Meta:
        db_table = 'discussions_comments'


def get_comments_of_single_discussion(discussion_id: int):
    discussion_comments = DbDiscussionComment.select().where(
        DbDiscussionComment.discussion_id == discussion_id)
    comments = []
    for discussion_comment in discussion_comments:
        comments.append(discussion_comment.__data__)
    return comments


def add_comment_to_discussion(
    discussion_id: int,
    current_user_id: str,
    content: str
):
    comment_object = DbDiscussionComment(
        discussion_id=discussion_id,
        timestamp=datetime.now(),
        author_user_id=current_user_id,
        content=content
    )

    comment_object.save()
    return comment_object.__data__


def delete_comment_from_discussion(
    discussion_id: int,
    comment_id: int
):
    comment = DbDiscussionComment.get(
        DbDiscussionComment.discussion_id == discussion_id, DbDiscussionComment.comment_id == comment_id)
    deleted_id = comment_id.__data__['comment_id']
    comment.delete_instance()
    return deleted_id
