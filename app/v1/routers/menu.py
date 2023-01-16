from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from ..crud import menu, submenu, dish
from ..schemas.menu import MenuGet, MenuCreate, MenuUpdate

router = APIRouter()


@router.get('/', response_model=List[MenuGet])
def read_menus(db: Session = Depends(get_db)):
    menus = menu.get_menus(db)
    return menus

@router.get("/{menu_id}", response_model=MenuGet)
def read_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu

@router.post("/", response_model=MenuGet, status_code=201)
def create_menu(m: MenuCreate, db: Session = Depends(get_db)):
    db_menu = menu.get_menu_by_title(db, title=m.title)
    if db_menu:
        raise HTTPException(status_code=400, detail="menu with this title already exist")
    return menu.create_menu(db=db, menu=m)

@router.patch("/{menu_id}", response_model=MenuGet)
def update_menu(menu_id: int, m: MenuUpdate, db: Session = Depends(get_db)):
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu.update_menu(db=db, menu=m)