from fastapi import HTTPException

from ..crud.menu_crud import MenuCrud
from ..schemas.menu import MenuCreate, MenuUpdate
from .cache_service import CacheService


class MenuService:
    def __init__(self, crud: MenuCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    async def get_menus(self):
        cached_data = await self.cache.get('menu_list')
        if cached_data:
            db_menus = cached_data
        else:
            db_menus = await self.crud.get_list()
            cached_data = await self.cache.set_all('menu_list', db_menus)
        return db_menus

    async def get_menu(self, menu_id: int):
        cached_data = await self.cache.get(f'menu_{menu_id}')
        if cached_data:
            db_menu = cached_data
        else:
            db_menu = await self.crud.get(menu_id)
            if db_menu is None:
                raise HTTPException(status_code=404, detail='menu not found')
            cached_data = await self.cache.set(f'menu_{menu_id}', db_menu)
        return db_menu

    async def create_menu(self, menu: MenuCreate):
        db_menu = await self.crud.get_by_title(title=menu.title)
        if db_menu:
            raise HTTPException(
                status_code=400,
                detail='menu with this title already exist',
            )
        await self.cache.delete('menu_list')
        return await self.crud.create(menu=menu)

    async def update_menu(self, menu_id: int, menu: MenuUpdate):
        db_menu = await self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        updated_menu = await self.crud.update(menu=menu, menu_id=menu_id)
        await self.cache.set(f'menu_{menu_id}', updated_menu)
        await self.cache.delete('menu_list')
        return updated_menu

    async def delete_menu(self, menu_id: int):
        db_menu = await self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        await self.crud.delete(menu_id=menu_id)
        await self.cache.delete(f'menu_{menu_id}')
        await self.cache.delete('menu_list')
        return {'status': 'true', 'message': 'The menu has been deleted'}
