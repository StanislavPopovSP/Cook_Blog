<h2 align="center">Cook blog</h2>


### Описание проекта:
Блог шеф-повара с рецептами.

Приложение позволяет взаимодействовать с аудиторией, находить любимый рецепт, комментировать его. 
Шеф-повар может выкладывать, изменять, удалять рецепт с его фотографией.

### Инструменты разработки

**Стек:**
- Python >= 3.9
- Django == 4.2
- sqlite3

## Разработка

##### 1) Поставить звездочку)

##### 2) Клонировать репозиторий

    https://github.com/StanislavPopovSP/Cook_Blog.git

##### 3) Создать виртуальное окружение

    cd cook
    
    python -m venv venv
    
##### 4) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 5) Устанавливить зависимости:

    pip install -r requirements.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver

##### 10) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin
