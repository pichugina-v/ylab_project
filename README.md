# API для проекта Меню ресторана.


# Начало работы:
* Создайте файл `.env` и заполните переменные окружения из примера`.env.example`
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
* Создайте файл `.env` и заполните переменные окружения из примера`.env.example`
* Выполните миграции
```bash
alembic upgrade head
```
* Запустите приложение
```bash
uvicorn main:app --reload
```