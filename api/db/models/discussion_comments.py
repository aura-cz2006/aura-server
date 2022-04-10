import datetime
from peewee import *
from datetime import datetime
import firebase_admin.auth as auth

from api.db.db_base_model import DbBaseModel
from .users import DbUser
from .discussions import DbDiscussion


class DbDiscussionComment(DbBaseModel):
    comment_id = IntegerField(primary_key=True)
    discussion_id = ForeignKeyField(DbDiscussion)
    timestamp = DateTimeField()
    author_user_id = CharField(max_length=255)
    content = CharField(max_length=255)

    class Meta:
        db_table = 'discussions_comments'


def get_comments_of_single_discussion(discussion_id: int):
    discussion_comments = DbDiscussionComment.select().where(
        DbDiscussionComment.discussion_id == discussion_id)
    comments = []
    for discussion_comment in discussion_comments:
        comment = dict(discussion_comment.__data__)

        user_id = comment["author_user_id"]
        user = auth.get_user(user_id)

        del comment["author_user_id"]
        comment.__setitem__("author", {
            "id": user_id,
            "displayName": user.display_name
        })
        comments.append(comment)
    return comments


def add_comment_to_discussion(
    discussion_id: int,
    current_user_id: str,
    content: str
):
    print(f"add_comment_to_discussion {current_user_id}")
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
