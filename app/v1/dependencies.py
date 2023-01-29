from fastapi import Depends
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.redis import get_redis
from .crud.dish_crud import DishCrud
from .crud.menu_crud import MenuCrud
from .crud.submenu_crud import SubmenuCrud
from .services.cache_service import CacheService
from .services.dish_service import DishService
from .services.menu_service import MenuService
from .services.submenu_service import SubmenuService


def get_cache(cache=Depends(get_redis)):
    return CacheService(cache)


def get_menu_crud(db: Session = Depends(get_db)):
    return MenuCrud(db)


def get_menu_service(
    crud: MenuCrud = Depends(get_menu_crud),
    cache: CacheService = Depends(get_cache),
):
    return MenuService(crud, cache)


def get_submenu_crud(db: Session = Depends(get_db)):
    return SubmenuCrud(db)


def get_submenu_service(
    crud: SubmenuCrud = Depends(get_submenu_crud),
    cache: CacheService = Depends(get_cache),
):
    return SubmenuService(crud, cache)


def get_dish_crud(db: Session = Depends(get_db)):
    return DishCrud(db)


def get_dish_service(
    crud: DishCrud = Depends(get_dish_crud),
    cache: CacheService = Depends(get_cache),
):
    return DishService(crud, cache=cache)
