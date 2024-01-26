from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'3d5ab4a6d6abc30f0788857a806e435d273e19d1772550736a5f3463944a37dd'
csrf = CSRFProtect(app)
""""
Генерация ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi'

@app.route('/data/')
def data():
    return 'Your data'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)