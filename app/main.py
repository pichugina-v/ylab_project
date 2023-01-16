from fastapi import FastAPI, APIRouter

from v1.routers import menu, submenu, dish


def create_app():
    app = FastAPI()
    app.include_router(
        menu.router,
        prefix='/api/v1/menus',
        tags=['menu']
    )
    app.include_router(
        submenu.router,
        prefix='/api/v1/menus/{menu_id}/submenus',
        tags=['submenu']
    )
    app.include_router(
        dish.router,
        prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes',
        tags=['dish']
    )
    return app 

app = create_app()