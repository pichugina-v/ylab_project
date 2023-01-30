from fastapi import HTTPException

from ..crud.menu_crud import MenuCrud
from ..schemas.menu import MenuCreate, MenuUpdate
from .cache_service import CacheService


class MenuService:
    def __init__(self, crud: MenuCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    def get_menus(self):
        cached_data = self.cache.get('menu_list')
        if cached_data:
            db_menus = cached_data
        else:
            db_menus = self.crud.get_list()
            cached_data = self.cache.set_all('menu_list', db_menus)
        return db_menus

    def get_menu(self, menu_id: int):
        cached_data = self.cache.get(f'menu_{menu_id}')
        if cached_data:
            db_menu = cached_data
        else:
            db_menu = self.crud.get(menu_id)
            if db_menu is None:
                raise HTTPException(status_code=404, detail='menu not found')
            cached_data = self.cache.set(f'menu_{menu_id}', db_menu)
        return db_menu

    def create_menu(self, menu: MenuCreate):
        db_menu = self.crud.get_by_title(title=menu.title)
        if db_menu:
            raise HTTPException(
                status_code=400,
                detail='menu with this title already exist',
            )
        self.cache.delete('menu_list')
        return self.crud.create(menu=menu)

    def update_menu(self, menu_id: int, menu: MenuUpdate):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        updated_menu = self.crud.update(menu=menu, menu_id=menu_id)
        self.cache.set(f'menu_{menu_id}', updated_menu)
        self.cache.delete('menu_list')
        return updated_menu

    def delete_menu(self, menu_id: int):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        self.crud.delete(menu_id=menu_id)
        self.cache.delete(f'menu_{menu_id}')
        self.cache.delete('menu_list')
        return {'status': 'true', 'message': 'The menu has been deleted'}
