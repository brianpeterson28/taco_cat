from flask import Flask, g, flash, redirect, url_for, render_template

from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)

import forms
import models 

app = Flask(__name__)
app.secret_key = 'akdjfkue17376348bfbndfs.nkasdfnj'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE 
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    tacos = models.Taco.select()
    if tacos.count() == 0:
        return "no tacos yet"
    else:
        return render_template('index.html', tacos=tacos)

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

@app.route('/taco', methods=['GET','POST'])
@login_required
def taco():
    form = forms.TacoForm()
    if form.validate_on_submit():
        models.Taco.create(user=g.user._get_current_object(),
                          protein=form.protein.data.strip(),
                          shell=form.shell.data.strip(),
                          cheese=form.cheese.data,
                          extras=form.extras.data.strip())
        return redirect(url_for('index'))
    return render_template('taco.html', form=form)
        
    
if __name__ == '__main__':
    pass