from flask import Flask, flash, redirect, url_for
import forms
import models 

app = Flask(__name__)
app.secret_key = 'akdjfkue17376348bfbndfs.nkasdfnj'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        models.User.create_user(email=form.email.data,
                                password=form.password.data)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    pass