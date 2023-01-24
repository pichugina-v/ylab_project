# API для проекта Меню ресторана.


# Начало работы:
* Создайте файл `.env` и заполните переменные окружения
```bash
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к базе данных>
POSTGRES_HOST=<хост>
POSTGRES_PORT=5432
POSTGRES_DB=<название базы данных>
POSTGRES_SERVICE=web_app_db
```
* Запустите приложение
```bash
docker-compose up -d
```
* Запустите тесты
```bash
docker-compose -f "docker-compose.tests.yaml" up
```

___
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
```
* Выполните миграции
```bash
alembic upgrade head
```
* Запустите приложение
```bash
 uvicorn main:app --reload
```