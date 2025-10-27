## 🚀 Установка проекта

1. Клонируйте репозиторий  
   `git clone https://github.com/AM-Kovalenko/TMS_django_shop.git`

2. Перейдите в каталог проекта  
   `cd TMS_django_shop`

3. Создайте виртуальное окружение  
   `python -m venv .venv`

4. Активируйте окружение  
   `source .venv/bin/activate`

5. Установите зависимости  
   `pip install -r requirements.txt`

6. Создайте базу данных PostgreSQL  
   Откройте терминал PostgreSQL и выполните команды:  
   ```sql
   psql -U postgres
   CREATE DATABASE mydb;
   \q

7. Настройте подключение к базе данных
В файле .env (создайте его в папке myproject/) добавьте строки:

DB_NAME=mydb
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

8. Примените миграции
python manage.py migrate

9.Запустите сервер разработки
python manage.py runserver

10 Перейдите в браузере по адресу:
http://127.0.0.1:8000/
