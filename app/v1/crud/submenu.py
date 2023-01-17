from sqlalchemy.orm import Session

from ..models.models import Submenu
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate


def get_submenu(db: Session, submenu_id: int):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()

def get_submenu_by_title(db: Session, title: str):
    return db.query(Submenu).filter(Submenu.title == title).first()

def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Submenu).offset(skip).limit(limit).all()

def create_submenu(db: Session, submenu: SubmenuCreate, menu_id: int):
    db_submenu = Submenu(
        title=submenu.title,
        description=submenu.description,
        menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu

def update_submenu(db: Session, submenu: SubmenuUpdate, submenu_id: int):
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    submenu_data = submenu.dict(exclude_unset=True)
    for key, value in submenu_data.items():
        setattr(db_submenu, key, value)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu

def delete_submenu(db: Session, submenu_id: int):
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    db.delete(db_submenu)
    db.commit()
