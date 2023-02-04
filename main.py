from fastapi import FastAPI

from app.v1.routers import dish, menu, submenu, db
from docs_info import description, tags_metadata, title


def create_app():
    app = FastAPI(
        docs_url='/api/docs',
        redoc_url='/api/redoc',
        title=title,
        description=description,
        version='0.0.1',
        openapi_tags=tags_metadata,
    )

    app.include_router(
        db.router,
        prefix='/api/v1/data',
        tags=['db_data']
    )
    app.include_router(
        menu.router,
        prefix='/api/v1',
        tags=['menus'],
    )
    app.include_router(
        submenu.router,
        prefix='/api/v1/menus/{menu_id}',
        tags=['submenus'],
    )
    app.include_router(
        dish.router,
        prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}',
        tags=['dishes'],
    )
    return app


app = create_app()
