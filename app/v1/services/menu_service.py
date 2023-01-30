from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from ..crud.menu_crud import MenuCrud
from ..schemas.menu import MenuCreate, MenuUpdate
from .cache_service import CacheService


class MenuService:
    def __init__(self, crud: MenuCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    def get_menus(self):
        # cached_data = self.cache.getall(url)
        # print('cached_list', cached_data, url)
        # if cached_data is not None:
        #     db_menus = cached_data
        # else:
        #     db_menus = self.crud.get_list()
        #     print('new_cache_list', jsonable_encoder(db_menus))
        #     cached_data = self.cache.set(url, jsonable_encoder(db_menus))
        # return db_menus
        return self.crud.get_list()

    def get_menu(self, menu_id: int, url):
        cached_data = self.cache.get(url)
        if cached_data:
            db_menu = cached_data
        else:
            db_menu = self.crud.get(menu_id)
            if db_menu is None:
                raise HTTPException(status_code=404, detail='menu not found')
            cached_data = self.cache.set(url, jsonable_encoder(db_menu))
        return db_menu

    def create_menu(self, menu: MenuCreate):
        db_menu = self.crud.get_by_title(title=menu.title)
        if db_menu:
            raise HTTPException(
                status_code=400,
                detail='menu with this title already exist',
            )
        return self.crud.create(menu=menu)

    def update_menu(self, menu_id: int, url, menu: MenuUpdate):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        updated_menu = self.crud.update(menu=menu, menu_id=menu_id)
        self.cache.set(url, jsonable_encoder(updated_menu))
        return updated_menu

    def delete_menu(self, menu_id: int, url):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        self.crud.delete(menu_id=menu_id)
        self.cache.delete(jsonable_encoder(url))
        return {'message': 'The menu has been deleted'}
