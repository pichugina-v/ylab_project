from fastapi import HTTPException

from ..crud.dish_crud import DishCrud
from ..schemas.dish import DishCreate, DishUpdate


class DishService:
    def __init__(self, crud: DishCrud):
        self.crud = crud

    def get_dishes(self):
        return self.crud.get_list()

    def get_dish(self, dish_id: int):
        db_dish = self.crud.get(dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail="dish not found")
        return db_dish

    def create_dish(self, submenu_id: int, dish: DishCreate):
        db_dish = self.crud.get_by_title(title=dish.title)
        if db_dish:
            raise HTTPException(
                status_code=400,
                detail='dish with this title already exist'
            )
        return self.crud.create(dish=dish, submenu_id=submenu_id)

    def update_dish(self, dish_id: int, submenu_id: int, dish: DishUpdate):
        db_dish = self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        return self.crud.update(dish=dish, dish_id=dish_id, submenu_id=submenu_id)
    
    def delete_dish(self, dish_id: int):
        db_dish = self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        self.crud.delete(dish_id=dish_id)
        return {'message': 'The dish has been deleted'}
