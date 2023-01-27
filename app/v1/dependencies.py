from fastapi import Depends
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..v1.crud.menu_crud import MenuCrud
from ..v1.crud.submenu_crud import SubmenuCrud
from ..v1.crud.dish_crud import DishCrud
from ..v1.services.menu_service import MenuService
from ..v1.services.submenu_service import SubmenuService
from ..v1.services.dish_service import DishService

def get_menu_crud(db: Session = Depends(get_db)):
    return MenuCrud(db=db)

def get_menu_service(crud: MenuCrud = Depends(get_menu_crud)):
    return MenuService(crud)

def get_submenu_crud(db: Session = Depends(get_db)):
    return SubmenuCrud(db=db)

def get_submenu_service(crud: SubmenuCrud = Depends(get_submenu_crud)):
    return SubmenuService(crud)

def get_dish_crud(db: Session = Depends(get_db)):
    return DishCrud(db=db)

def get_dish_service(crud: SubmenuCrud = Depends(get_dish_crud)):
    return DishService(crud)