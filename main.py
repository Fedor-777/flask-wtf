import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def main():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)

@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)

@app.route('/traning/<prof>')
def traning(prof):
    if "инженер" in prof:
        param = {}
        param['text'] = "Инженерные тренажеры"
        param['filepath'] = '/static/image/ик.jfif'

    if "строитель" in prof:
        param = {}
        param['text'] = "Научные симуляторы"
        param['filepath'] = '/static/image/нс.jfif'

    return render_template('ex2.html', **param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')