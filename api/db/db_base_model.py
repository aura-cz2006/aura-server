from peewee import *
from .database import conn


class DbBaseModel(Model):
    class Meta:
        database = conn
