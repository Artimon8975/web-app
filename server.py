from random import randint
from flask import Flask, session, redirect, url_for, request, render_template
from main_db_controll import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


# Главная страница с формой
def index():
    return render_template('main.html')


# Обработка данных формы и сохранение в БД
def answer():
    if request.method == 'POST':
        # Получаем данные из формы
        data = tuple(request.form.values())
        list_color = request.form.getlist('color')
        print(list_color)
        
        # Сохраняем данные в базу данных
        db.add_data(data, list_color)
        
        # Получаем все записи из базы данных для отображения
        info = db.get_data()
        
        # Перенаправляем на страницу с результатом
        return render_template('answer.html', obj=info)
    
    return 'Не POST запрос'


# Страница с результатами
def result():
    info = db.get_data()
    return render_template('answer.html', obj=info)


# Создание URL для разных страниц
app.add_url_rule('/', 'index', index)  # Главная страница с формой
app.add_url_rule('/answer', 'answer', answer, methods=['POST'])  # Обработка данных формы
app.add_url_rule('/result', 'result', result)  # Страница с результатами


if __name__ == '__main__':
    # Запуск веб-сервера
    app.run(debug=True)
