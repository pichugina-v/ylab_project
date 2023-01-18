from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from ..crud import dish
from ..schemas.dish import DishGet, DishCreate, DishUpdate

router = APIRouter()

@router.get('/dishes', response_model=List[DishGet])
def read_dishes(db: Session = Depends(get_db)):
    dishes = dish.get_dishes(db)
    return dishes

@router.get("/dishes/{dish_id}", response_model=DishGet)
def read_dish(dish_id: int, db: Session = Depends(get_db)):
    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish

@router.post("/dishes", response_model=DishGet, status_code=201)
def create_dish(submenu_id: int, d: DishCreate, db: Session = Depends(get_db)):
    db_dish = dish.get_dish_by_title(db, title=d.title)
    if db_dish:
        raise HTTPException(status_code=400, detail="dish with this title already exist")
    return dish.create_dish(
        db=db, dish=d, submenu_id=submenu_id
    )

@router.patch("/dishes/{dish_id}", response_model=DishGet)
def update_dish(dish_id: int, d: DishUpdate, db: Session = Depends(get_db)):
    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return dish.update_dish(db=db, dish=d, dish_id=dish_id)

@router.delete("/dishes/{dish_id}")
def delete_submenu(dish_id: int, db: Session = Depends(get_db)):
    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    dish.delete_dish(db=db, dish_id=dish_id)
    return {"message": "The dish has been deleted"}
    