# API для проекта Меню ресторана. Учебный проект Ylab. 


# Начало работы:
* Склонируйте репозиторий `ylab_project`
```bash
git clone https://github.com/pichugina-v/ylab_project.git
```
* Создайте вирутальное окружение
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
POSTGRES_HOST=<хост>
POSTGRES_PORT=5432
POSTGRES_DB=<название базы данных>
```
* Подключите аlembic к базе данных. В файле `alembic.ini` заполните переменную `sqlalchemy.url` и выполните миграции
```python
sqlalchemy.url = driver://user:pass@localhost/dbname
```
```bash
alembic upgrade head
```
* Запустите приложение
```bash
 uvicorn main:app --reload
```