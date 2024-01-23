from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def my_base():
    return render_template('new_base.html')


@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_age = request.form.get('age')
        if int(user_age) <= 18:
            return "Извините Вам еще рано"
        else:
            return render_template('user.html')



if __name__ == '__main__':
    app.run(debug=True)