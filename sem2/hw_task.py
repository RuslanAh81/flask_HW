from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)
app.secret_key = '8b1ae9e80d43bf3f9d97f68f5490a8134f7961e613ca594fe9945e3080f5befb'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        new_name = session['username']
       # Почему не работает set_cookie
        set_cookie()
        print(new_name)
        return redirect(url_for('hw_main', name=new_name))

    return render_template('username_form.html')


@app.route('/set_cookie/')
def set_cookie():
    print('Hello')
    response = make_response("Cookie установлены")
    response.set_cookie('username', 'Agafon')
    return response


@app.route('/del_cookie/')
def del_cookie():
    print('Hello')
    response = make_response("Cookie удалены")
    response.set_cookie('username', 'Agafon', max_age=0)
    return response

@app.route('/hwmain/<name>')
def hw_main(name):
    context = {
        'name': name
    }
    # print(name)
    return render_template('hwmain.html', **context)

# @app.route('/logout/')
# def logout():
#     # session.pop('username', None)
#     request.delete_cookie('username')
#     return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)