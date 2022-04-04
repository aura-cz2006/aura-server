
from datetime import datetime
from api.models.comments_model import CommentItem



sample_comment_data = [
    CommentItem(
        id= "1",
        text= "Fantastico!",
        user= "1",
        timestamp= datetime.fromisoformat("2019-12-04"),
    ),
    CommentItem(
        id= "2",
        text= "This is such a good thread!",
        user= "2",
        timestamp= datetime.fromisoformat("2019-12-04"),
    ),
    CommentItem(
        id= "3",
        text= "=D",
        user= "3",
        timestamp= datetime.fromisoformat("2019-12-04"),
    ),
    CommentItem(
        id= "4",
        text= "Wow I didnt know this =p thanks for sharing",
        user= "4",
        timestamp= datetime.fromisoformat("2019-12-04"),
    ),
    CommentItem(
        id= "5",
        text= "Coooooool beans!",
        user= "5",
        timestamp= datetime.fromisoformat("2019-12-04"),
    )
]