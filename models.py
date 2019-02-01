from peewee import *

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

DATABASE = SqliteDatabase('taco.db')

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=20)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(email=email, 
                           password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError("User already exists.")

class Taco(Model):
    user = ForeignKeyField(User, related_name='tacos')
    protein = TextField()
    shell = TextField()
    cheese = BooleanField(default=True)
    extras = TextField()

    class Meta:
        database = DATABASE
        