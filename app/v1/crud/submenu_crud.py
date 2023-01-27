from sqlalchemy.orm import Session

from ..models.models import Submenu
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate


class SubmenuCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def get(self, submenu_id: int):
        db_submenu = self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        if db_submenu is None:
            return None
        return db_submenu

    def get_by_title(self, title: str):
        db_submenu = self.db.query(Submenu).filter(Submenu.title == title).first()
        if db_submenu is None:
            return None
        return db_submenu

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(Submenu).offset(skip).limit(limit).all()

    def create(self, menu_id: int, submenu: SubmenuCreate):
        db_submenu = Submenu(
            title=submenu.title,
            description=submenu.description,
            menu_id=menu_id)
        self.db.add(db_submenu)
        self.db.commit()
        self.db.refresh(db_submenu)
        return db_submenu

    def update(self, submenu_id: int, menu_id: int, submenu: SubmenuUpdate):
        db_submenu = self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        submenu_data = submenu.dict(exclude_unset=True)
        for key, value in submenu_data.items():
            setattr(db_submenu, key, value)
        self.db.add(db_submenu)
        self.db.commit()
        self.db.refresh(db_submenu)
        return db_submenu

    def delete(self, submenu_id: int):
        db_submenu = self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        self.db.delete(db_submenu)
        self.db.commit()
