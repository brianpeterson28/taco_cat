from peewee import *

DATABASE = SqliteDatabase('taco.db')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=20)

    class Meta:
        database = DATABASE