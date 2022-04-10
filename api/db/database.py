import os
from peewee import MySQLDatabase

print(f"db hostname is: {os.getenv('MYSQL_HOSTNAME')}")

password = os.getenv('MYSQL_PASSWORD')
if password == None:
    raise Exception(
        "No MySQL passwrod was provided via environment variables")
db_name = os.getenv('MYSQL_DATABASE') or "db"
host = os.getenv('MYSQL_HOSTNAME') or "localhost"

conn = MySQLDatabase(
    db_name,
    user="root",
    password=password,
    host=host
    # host='172.28.1.2'
    # host='localhost'
)
