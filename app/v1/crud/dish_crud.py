from sqlalchemy.orm import Session

from ..models.models import Dish
from ..schemas.dish import DishCreate, DishUpdate


class DishCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def get(self, dish_id: int):
        db_dish = self.db.query(Dish).filter(Dish.id == dish_id).first()
        if db_dish is None:
            return None
        return db_dish

    def get_by_title(self, title: str):
        db_dish = self.db.query(Dish).filter(Dish.title == title).first()
        if db_dish is None:
            return None
        return db_dish

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(Dish).offset(skip).limit(limit).all()

    def create(self, submenu_id: int, dish: DishCreate):
        db_dish = Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            submenu_id=submenu_id)
        self.db.add(db_dish)
        self.db.commit()
        self.db.refresh(db_dish)
        return db_dish

    def update(self, dish_id: int, submenu_id: int, dish: DishUpdate):
        db_dish = self.db.query(Dish).filter(Dish.id == dish_id).first()
        dish_data = dish.dict(exclude_unset=True)
        for key, value in dish_data.items():
            setattr(db_dish, key, value)
        self.db.add(db_dish)
        self.db.commit()
        self.db.refresh(db_dish)
        return db_dish

    def delete(self, dish_id: int):
        db_dish = self.db.query(Dish).filter(Dish.id == dish_id).first()
        self.db.delete(db_dish)
        self.db.commit()
