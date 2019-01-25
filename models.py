from peewee import *

from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('taco.db')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=20)

    class Meta:
        database = DATABASE

@classmethod
def create_user(cls, email, password):
    try:
        with DATABASE.transaction():
            cls.create(email=email, password=password)
    except IntegrityError:
        raise ValueError("User already exists.")