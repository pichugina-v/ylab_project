# API для проекта меню ресторана. учебный проект Ylab. 


# Начало работы:
* Склонируйте репозиторий `ylab_project`
```bash
git clone https://github.com/pichugina-v/ylab_project.git
```
*Создайте вирутальное окружение
```bash
python -m venv venv
```
* Установите зависимости
```bash
pip install -r requirements.txt
```
* Перейдите в директорию app/
```bash
cd app/
```
* В директории /app создайте файл `.env` и заполните переменные окружения
```bash
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к базе данных>
POSTGRES_HOST=0.0.0.0
POSTGRES_PORT=5432
POSTGRES_DB=<название бд>
```
* Подключите аlembic к базе данных
```
* В файле `alembic.ini` заполните переменную `sqlalchemy.url` 
* Выполните миграции
```
alembic revision --autogenerate -m "create tables"
python -m alembic upgrade head
```
* Запустите приложение
```bash
 uvicorn main:app --reload
```