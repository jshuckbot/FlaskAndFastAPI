from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask('__main__')


@app.route('/')
def main():
    context = {
        'title': 'Главная',
    }

    return render_template('page_1.html', **context)


@app.route('/cookie/', methods=['GET', 'POST'])
def cookie():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        resp = make_response(redirect(url_for('welcome')))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)
       
        return resp
    return redirect(url_for('main'))


@app.route('/welcome/')
def welcome():
    name = request.cookies.get('name')
    context = {
        'title': 'Добро пожаловать!',
        'name': name,
    }
    return render_template('welcome.html', **context)


@app.route('/exit/')
def exit():
    resp = make_response(redirect(url_for('main')))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    
    return resp


if __name__ == '__main__':
    app.run()
