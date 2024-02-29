from flask import Flask
from flask import render_template, url_for
from flask import request


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


@app.route('/promotion_image')
def poster():
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <div>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename="img/marc.png")}">
                            <div class="texts">
                                <p>Человечество вырастает из детства.</p>
                                <p>Человечеству мала одна планета.</p>
                                <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                                <p>И начнем с Марса!</p>
                                <p>Присоединяйся!</p>
                            </div>
                        </div>
                    </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="text-center">Анкета претендента</h1>
                            <h4 class="text-center">на участие в миссии</h4>
                            <div class="mt-5">
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control mb-1" id="secondname" placeholder="Введите фамилию" name="secondname">
                                    <input type="text" class="form-control mb-3" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control mb-3" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group mb-2">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее Профессиональное</option>
                                          <option>Среднее общее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group form-check">
                                        <label class="form-check-label" for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check form-group" id="prof">
                                            <input type="checkbox" class="form-check-input" id="sai" name="sai">
                                            <label for="sai">Инженер-исследователь</label>
                                            <label for="build">Инженер-строитель</label>
                                            <input type="checkbox" class="form-check-input" id="build" name="build">
                                            <label for="fly">Пилот</label>
                                            <input type="checkbox" class="form-check-input" id="fly" name="fly">
                                            <label for="weat">Метеоролог</label>
                                            <input type="checkbox" class="form-check-input" id="weat" name="weat">
                                            <label for="life">Инженер по жизнеобеспечению</label>
                                            <input type="checkbox" class="form-check-input" id="life" name="life">
                                            <label for="rad">Инженер по радиационной защите</label>
                                            <input type="checkbox" class="form-check-input" id="rad" name="rad">
                                            <label for="doc">Врач</label>
                                            <input type="checkbox" class="form-check-input" id="doc" name="doc">
                                            <label for="ekz">Экзобиолог</label>
                                            <input type="checkbox" class="form-check-input" id="ekz" name="ekz">
                                        </div>
                                    </div>
                                    <div class="form-group mt-2">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group mt-2">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group mt-2">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check mt-2">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary mt-2">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choiches(planet_name):
    data = {
        "planet_name": planet_name
    }
    return render_template("work.html", data=data)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    data = {
        "nickname": nickname,
        "level": level,
        "rating": rating
    }
    return render_template("result.html", data=data)


@app.route("/carousel")
def slider():
    return f"""
    <head>
        <title>Пейзажи Марса</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body>
        <h1 class="text-center">Пейзажи Марса</h1>
        <div id="myCarousel" class="carousel slide mb-5" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2" class=""></button>
            <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3" class="active" aria-current="true"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item">
              <img class="bd-placeholder-img" style="object-fit: cover; height: 100vh;" src="{url_for('static', filename="img/marc1.png")}" width="100%" height="80vh" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
            </div>
            <div class="carousel-item">
              <img class="bd-placeholder-img" style="object-fit: cover; height: 100vh;" src="{url_for('static', filename="img/marc2.png")}" width="100%" height="80vh" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
            </div>
            <div class="carousel-item active">
              <img class="bd-placeholder-img" style="object-fit: cover; height: 100vh;" src="{url_for('static', filename="img/marc3.png")}" width="100%" height="80vh" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js"></script>
    </body>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')