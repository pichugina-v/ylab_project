from sqlalchemy.orm import Session

from ..models.models import Dish
from ..schemas.dish import DishCreate, DishUpdate


def get_dish(db: Session, dish_id: int):
    return db.query(Dish).filter(Dish.id == dish_id).first()

def get_dish_by_title(db: Session, title: str):
    return db.query(Dish).filter(Dish.title == title).first()

def get_dishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Dish).offset(skip).limit(limit).all()

def create_dish(db: Session, dish: DishCreate, submenu_id: int):
    db_dish = Dish(
        title=dish.title,
        price=dish.price,
        description=dish.description,
        submenu_id=submenu_id
    )
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def update_dish(db: Session, dish: DishUpdate, dish_id: int):
    db_dish = db.query(Dish).filter(Dish.id == dish_id).first()
    dish_data = dish.dict(exclude_unset=True)
    for key, value in dish_data.items():
        setattr(db_dish, key, value)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def delete_dish(db: Session, dish_id: int):
    db_dish = db.query(Dish).filter(Dish.id == dish_id).first()
    db.delete(db_dish)
    db.commit()
