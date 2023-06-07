<h2 align="center">Cook blog</h2>


### Описание проекта:
Блог шеф-повара с его рецептами.

Приложение позволяет взаимодействовать с аудиторией.
Пользователь может находить любимый рецепт через поиск, меню, по разным категориям, комментировать сам рецепт. 
Есть форма обратной связи с Шев поваром через админ панель, а так же его контактные данные.
Шеф-повар может выкладывать, изменять, удалять рецепт с его фотографией, выкладывать галерею фотографий из админ панел.

### Инструменты разработки

**Стек:**
- Python >= 3.9
- Django == 4.2
- sqlite3

## Установка

##### 1) Клонировать репозиторий

    https://github.com/StanislavPopovSP/Cook_Blog.git

##### 2) Создать виртуальное окружение

    cd cook
    
    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver

##### 8) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin
