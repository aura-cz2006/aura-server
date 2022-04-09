import os
from peewee import MySQLDatabase

user = 'user'
password = 'password'
db_name = 'db'

conn = MySQLDatabase(
    db_name,
    user=user,
    password=password,
    host=os.getenv('MYSQL_HOSTNAME')
    # host='172.28.1.2'
    # host='localhost'
)
