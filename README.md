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
```
* В файле `alembic.ini` заполните переменную `sqlalchemy.url` и выполните миграции
```bash
alembic upgrade head
```
* Запустите приложение
```bash
 uvicorn main:app --reload
```
