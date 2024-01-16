from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/shop_main/')
def get_html():
    context = {'title': 'Главная'}
    return render_template('new_shop_main.html', **context)


@app.route('/cloth_main/')
def get_cloth():
    context = {'title': 'Одежда'}
    return render_template('cloth_main.html', **context)


@app.route('/shoes_main/')
def get_shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes_main.html', **context)


@app.route('/bags_main/')
def get_bags():
    context = {'title': 'Сумки'}
    return render_template('bags_main.html', **context)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
