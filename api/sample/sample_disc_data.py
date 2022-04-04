from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_comment_data import sample_comment_data
from datetime import datetime

comments = sample_comment_data

sample_disc_data = [
    DiscussionItem(
        id="1",
        topic=Topics.general,
        content="Some content for the discussion",
        title="Where is the cleanest toilet in Singapore?",
        comments=comments,
        date=datetime.fromisoformat("2019-12-04"),
        userID="1",
        likedBy=["1","2","3"],
    ),
    DiscussionItem(
        id="2",
        topic=Topics.general,
        content="Some content for the discussion",
        title="Best barber in the East?",
        comments=comments,
        date=datetime.fromisoformat("2019-12-04"),
        userID="2",
        likedBy=["1","2","3"],
    ),
    DiscussionItem(
        id="3",
        topic=Topics.nature,
        content="Some content for the discussion",
        title="New exhibit in Punggol Park in Singapore",
        comments=comments,
        date=datetime.fromisoformat("2019-12-04"),
        userID="3",
        likedBy=["1","2","3"],
    )
]
