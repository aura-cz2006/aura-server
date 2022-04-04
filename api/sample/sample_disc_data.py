from api.models.discussions_model import DiscussionItem, Topics
from api.sample.sample_comment_data import sample_comment_data
from datetime import datetime

comments =  sample_comment_data

sample_disc_data = [
    DiscussionItem(
        id="1",
        topic=Topics.general,
        title="Where is the cleanest toilet in Singapore?",
        comments= comments,
        date=datetime.fromisoformat("2019-12-04")

    ),
    DiscussionItem(
        id="2",
        topic=Topics.general,
        title="Best barber in the East?",
        comments= comments,
        date= datetime.fromisoformat("2019-12-04"),
    ),
    DiscussionItem(
        id="3",
        topic=Topics.nature,
        title="New exhibit in Punggol Park in Singapore",
        comments= comments,
        date= datetime.fromisoformat("2019-12-04"),
    )
]