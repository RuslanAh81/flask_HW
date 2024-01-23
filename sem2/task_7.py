from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def my_base():
    return render_template('calculate.html')

@app.route('//<numb>/')
def my_squere(numb):
    return f'Квадрат числа:{numb} равен {int(numb) ** 2}'

@app.route('/auth/', methods=['GET', 'POST'])
def summa():
    if request.method == 'POST':
        numb = request.form.get('number')
        return redirect(url_for('my_squere', numb=numb))


if __name__ == '__main__':
    app.run(debug=True)