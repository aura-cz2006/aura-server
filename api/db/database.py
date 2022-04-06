from peewee import MySQLDatabase

user = 'user'
password = 'password'
db_name = 'db'

conn = MySQLDatabase(
    db_name,
    user=user,
    password=password,
    host='172.17.0.1'
    # host='localhost'
)
