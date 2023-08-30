import datetime

from flask import Flask, render_template

app = Flask('__main__')


@app.route('/')
def main():
    context = {
        'title': 'Главная',
        'description': 'Главная страница Интернет магазина',
    }

    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {
        'title': 'Одежда',
        'description': 'Страница одежды',
    }

    return render_template('clothes.html', **context)


@app.route('/jackets/')
def jackets():
    context = {
        'title': 'Куртки',
        'description': 'Страница курток',
    }

    return render_template('jacket.html', **context)


@app.route('/shoes/')
def shoes():
    context = {
        'title': 'Обувь',
        'description': 'Страница обуви',
    }

    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
