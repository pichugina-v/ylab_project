from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from ..crud.dish_crud import DishCrud
from ..schemas.dish import DishCreate, DishUpdate
from .cache_service import CacheService


class DishService:
    def __init__(self, crud: DishCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    def get_dishes(self):
        return self.crud.get_list()

    def get_dish(self, dish_id: int, url):
        cached_data = self.cache.get(url)
        if cached_data:
            db_dish = cached_data
        else:
            db_dish = self.crud.get(dish_id)
            if db_dish is None:
                raise HTTPException(status_code=404, detail='dish not found')
            self.cache.set(url, jsonable_encoder(db_dish))
        return db_dish

    def create_dish(self, submenu_id: int, dish: DishCreate):
        db_dish = self.crud.get_by_title(title=dish.title)
        if db_dish:
            raise HTTPException(
                status_code=400,
                detail='dish with this title already exist',
            )
        return self.crud.create(
            dish=dish,
            submenu_id=submenu_id,
        )

    def update_dish(
        self, dish_id: int,
        submenu_id: int, url, dish: DishUpdate,
    ):
        db_dish = self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        self.cache.delete(jsonable_encoder(url))
        return self.crud.update(
            dish=dish,
            dish_id=dish_id,
            submenu_id=submenu_id,
        )

    def delete_dish(self, dish_id: int, url):
        db_dish = self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        self.crud.delete(dish_id=dish_id)
        self.cache.delete(jsonable_encoder(url))
        return {'message': 'The dish has been deleted'}
