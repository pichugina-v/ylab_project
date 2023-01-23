# API для проекта Меню ресторана.


# Начало работы:
* Создайте вирутальное окружение и установите зависимости
```bash
python -m venv venv
pip install -r requirements.txt
```
* Создайте файл `.env` и заполните переменные окружения
```bash
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к базе данных>
POSTGRES_HOST=<хост>
POSTGRES_PORT=5432
POSTGRES_DB=<название базы данных>
POSTGRES_SERVICE=web_app_db
<<<<<<< HEAD
=======
```
* Запустите приложение
```bash
docker-compose up -d
>>>>>>> c7c5fbe86dc40fbdfb81fc7f3da17acd9ded33c2
```
* Запустите тесты
```bash
<<<<<<< HEAD
docker-compose up -d
=======
docker-compose -f "docker-compose.tests.yaml" up
>>>>>>> c7c5fbe86dc40fbdfb81fc7f3da17acd9ded33c2
```
* Запустите тесты
```bash
docker-compose -f "docker-compose.tests.yaml" up
```