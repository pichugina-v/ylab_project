from sqlalchemy.orm import Session

from ..models.models import Menu
from ..schemas.menu import MenuCreate, MenuUpdate


class MenuCrud:
    def __init__(self, db: Session):
        self.db = db

    def get(self, menu_id: int):
        db_menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        if db_menu is None:
            return None
        return db_menu

    def get_by_title(self, title: str):
        db_menu = self.db.query(Menu).filter(Menu.title == title).first()
        if db_menu is None:
            return None
        return db_menu

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(Menu).offset(skip).limit(limit).all()

    def create(self, menu: MenuCreate):
        db_menu = Menu(title=menu.title, description=menu.description)
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return db_menu

    def update(self, menu_id: int, menu: MenuUpdate):
        db_menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        menu_data = menu.dict(exclude_unset=True)
        for key, value in menu_data.items():
            setattr(db_menu, key, value)
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return db_menu

    def delete(self, menu_id: int):
        db_menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        self.db.delete(db_menu)
        self.db.commit()
