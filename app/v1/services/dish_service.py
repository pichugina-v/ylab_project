from fastapi import HTTPException

from ..crud.dish_crud import DishCrud
from ..schemas.dish import DishCreate, DishUpdate
from .cache_service import CacheService


class DishService:
    def __init__(self, crud: DishCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    async def get_dishes(self):
        # cached_data = self.cache.get('dish_list')
        # if cached_data:
        #     db_dishes = cached_data
        # else:
        db_dishes = await self.crud.get_list()
        # cached_data = self.cache.set_all('dish_list', db_dishes)
        return db_dishes

    async def get_dish(self, dish_id: int):
        # cached_data = self.cache.get(f'dish_{dish_id}')
        # if cached_data:
        #     db_dish = cached_data
        # else:
        db_dish = await self.crud.get(dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
            # self.cache.set(f'dish_{dish_id}', db_dish)
        return db_dish

    async def create_dish(
        self,
        menu_id: int,
        submenu_id: int,
        dish: DishCreate,
    ):
        db_dish = await self.crud.get_by_title(title=dish.title)
        if db_dish:
            raise HTTPException(
                status_code=400,
                detail='dish with this title already exist',
            )
        # self.cache.delete(f'menu_{menu_id}')
        # self.cache.delete(f'submenu_{submenu_id}')
        # self.cache.delete('menu_list')
        # self.cache.delete('submenu_list')
        # self.cache.delete('dish_list')
        return await self.crud.create(
            dish=dish,
            submenu_id=submenu_id,
        )

    async def update_dish(
        self, dish_id: int,
        submenu_id: int,
        dish: DishUpdate,
    ):
        db_dish = await self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        updated_dish = await self.crud.update(
            dish=dish,
            dish_id=dish_id,
            submenu_id=submenu_id,
        )
        # self.cache.set(f'dish_{dish_id}', updated_dish)
        # self.cache.delete('dish_list')
        return updated_dish

    async def delete_dish(
            self, menu_id: int,
            submenu_id: int, dish_id: int,
    ):
        db_dish = await self.crud.get(dish_id=dish_id)
        if db_dish is None:
            raise HTTPException(status_code=404, detail='dish not found')
        await self.crud.delete(dish_id=dish_id)
        # self.cache.delete(f'menu_{menu_id}')
        # self.cache.delete(f'submenu_{submenu_id}')
        # self.cache.delete(f'dish_{dish_id}')
        # self.cache.delete('menu_list')
        # self.cache.delete('submenu_list')
        # self.cache.delete('dish_list')
        return {'status': 'true', 'message': 'The menu has been deleted'}
