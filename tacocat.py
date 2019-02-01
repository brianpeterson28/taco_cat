from flask import Flask, flash, redirect, url_for, render_template

from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)

import forms
import models 

app = Flask(__name__)
app.secret_key = 'akdjfkue17376348bfbndfs.nkasdfnj'

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(email=form.email.data,
                                password=form.password.data)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            pass
        else:
            user = models.User.get(models.User.email == form.email.data)
            login_user(user)
            return redirect(url_for('index'))
        return render_template('login.html', form=form)
    
if __name__ == '__main__':
    pass