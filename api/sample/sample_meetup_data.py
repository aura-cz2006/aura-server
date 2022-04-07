
from api.sample.sample_comment_data import sample_comment_data
from datetime import datetime
from api.models.meetups_model import MeetupItem


comments = sample_comment_data

sample_meetup_data = [
    MeetupItem(
        title='Badminton game @ bishan',
        description='Is anyone up for a game of badminton? For beginners!',
        createdAt=datetime.fromisoformat("2020-06-04"),
        meetupTime=datetime.fromisoformat("2022-06-04"),
        location={'lat': 1.3526, 'lng': 103.8352},
        id='1',
        userID='1',
        maxAttendees=15,
        rsvpAttendees=["1", "2", "3"],
        comments=comments,
        isCancelled=False,
    ),
    MeetupItem(
        title='Friendly neighbourhood get together',
        description='Anybody in their 20s interested to be friends?',
        createdAt=datetime.fromisoformat("2020-06-04"),
        meetupTime=datetime.fromisoformat("2022-06-04"),
        location={'lat': 1.26430, 'lng': 103.82231},
        id='2',
        userID='3',
        maxAttendees=8,
        rsvpAttendees=["2", "3", "4"],
        comments=comments,
        isCancelled=False,
    ),
    MeetupItem(
        title='Steamboat for CNY',
        description='Opening my house to anyone!',
        createdAt=datetime.fromisoformat("2020-06-04"),
        meetupTime=datetime.fromisoformat("2022-06-04"),
        location={'lat': 1.28672, 'lng': 103.82772},
        id='3',
        userID='3',
        maxAttendees=5,
        rsvpAttendees=["3", "4", "5"],
        comments=comments,
        isCancelled=False,
    ),
    MeetupItem(
        title='Looking for skating buddies',
        description='Recently picked up skating!',
        createdAt=datetime.fromisoformat("2020-06-04"),
        meetupTime=datetime.fromisoformat("2022-06-04"),
        location={'lat': 1.3526, 'lng': 103.8352},
        id='4',
        userID='4',
        maxAttendees=8,
        rsvpAttendees=["2", "3", "4"],
        comments=comments,
        isCancelled=False,
    )
]
