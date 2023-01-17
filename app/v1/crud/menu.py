from sqlalchemy.orm import Session

from ..models.models import Menu, Submenu
from ..schemas.menu import MenuCreate, MenuUpdate


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def get_menu_by_title(db: Session, title: str):
    return db.query(Menu).filter(Menu.title == title).first()

def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Menu).offset(skip).limit(limit).all()

def create_menu(db: Session, menu: MenuCreate):
    db_menu = Menu(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def update_menu(db: Session, menu: MenuUpdate, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    menu_data = menu.dict(exclude_unset=True)
    for key, value in menu_data.items():
        setattr(db_menu, key, value)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def delete_menu(db: Session, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    db.delete(db_menu)
    db.commit()
