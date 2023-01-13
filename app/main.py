from fastapi import FastAPI
from db.sqlalchemy_base import db

def create_app():
    app = FastAPI()
    db.init_app(app)

    return app

app = create_app()