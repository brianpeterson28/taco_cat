from flask_wtf import Form
from wtforms.validators import (DataRequired, Email,
                                Length, EqualTo)
from wtforms import StringField, PasswordField, TextAreaField, BooleanField

class RegisterForm(Form):

    email = StringField('Email',
                         validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                              validators=[DataRequired(),
                                          Length(min=2),
                                          EqualTo('password2')])

    password2 = PasswordField('Confirm Password',
                               validators=[DataRequired()])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class TacoForm(Form):
    protein = StringField('Protein', validators=[DataRequired()])
    shell = StringField('Shell', validators=[DataRequired()])
    cheese = BooleanField('Cheese', validators=[DataRequired()])
    extras = StringField('Extras', validators=[DataRequired()])
