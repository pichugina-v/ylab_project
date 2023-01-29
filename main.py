from fastapi import FastAPI

from app.v1.routers import dish, menu, submenu


def create_app():
    app = FastAPI(docs_url='/api/docs', redoc_url='/api/redoc')
    app.include_router(
        menu.router,
        prefix='/api/v1',
        tags=['menu'],
    )
    app.include_router(
        submenu.router,
        prefix='/api/v1/menus/{menu_id}',
        tags=['submenu'],
    )
    app.include_router(
        dish.router,
        prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}',
        tags=['dish'],
    )
    return app


app = create_app()
