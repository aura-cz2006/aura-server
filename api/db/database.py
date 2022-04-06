from peewee import MySQLDatabase

user = 'user'
password = 'password'
db_name = 'db'

conn = MySQLDatabase(
    db_name,
    user=user,
    password=password,
    host='localhost'
)
