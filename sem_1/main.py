from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/main/')
def get_html():
    context = {'title': 'Главная'}
    return render_template('new_main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('new_data.html', **context)


@app.route('/contacts/')
def my_contacts():
    _users = [{'name': 'Козлов А.М',
               'mail': 'a@mail.ru',
               'phone': '1234'},
              {'name': 'Конь Б.М',
               'mail': 'B@mail.ru',
               'phone': '12345'},
              {'name': 'Рыльев С.В',
               'mail': 'c@mail.ru',
               'phone': '123456'},
              ]
    context = {'users': _users, 'title': 'Для связи'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
