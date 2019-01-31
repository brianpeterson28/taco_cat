from flask_wtf import Form
from wtforms.validators import (DataRequired, Email,
                                Length, EqualTo)
from wtforms import StringField, PasswordField, TextAreaField

class RegisterForm(Form):

    email = StringField('Email',
                         validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                              validators=[DataRequired(),
                                          Length(min=2),
                                          EqualTo('password2')])

    password2 = PasswordField('Confirm Password',
                               validators=[DataRequired()])