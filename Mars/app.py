from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)


@app.route('/')
def name_mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def name_slang():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return """
    <p>
        Человечество вырастает из детства.<br><br>
        Человечеству мала одна планета.<br><br>
        Мы сделаем обитаемыми безжизненные пока планеты.<br><br>
        И начнем с Марса!<br><br>
        Присоединяйся!
    </p>
    """


@app.route("/image_mars")
def image():
    return f"""
    <title>Привет, Марс!</title>
    <article>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename="img/marc.png")}">
        <p>Вот она какая, красная планета</p>
    </article>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')