
# НЕ успеваю, не все сделал, запутался!!


from flask import Flask, render_template, request
from models import db, User
from forms import LoginForm, RegistrationForm

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'3d5ab4a6d6abc30f0788857a806e435d273e19d1772550736a5f3463944a37dd'
csrf = CSRFProtect(app)

db.init_app(app)

@app.route('/')
def index():
    return 'HII'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok')


@app.cli.command("create-users")
def create_user():
    from models import User
    db.session.add(User(name='name', email='name@email.com'))

    db.session.commit()
    print('User added')


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



if __name__ == "__main__":
    app.run(port=8080, debug=True)