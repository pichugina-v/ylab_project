from fastapi import HTTPException

from ..crud.submenu_crud import SubmenuCrud
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate
from .cache_service import CacheService


class SubmenuService:
    def __init__(self, crud: SubmenuCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    def get_submenus(self):
        cached_data = self.cache.get('submenu_list')
        if cached_data:
            db_submenus = cached_data
        else:
            db_submenus = self.crud.get_list()
            cached_data = self.cache.set_all('submenu_list', db_submenus)
        return db_submenus

    def get_submenu(self, submenu_id: int):
        cached_data = self.cache.get(f'submenu_{submenu_id}')
        if cached_data:
            db_submenu = cached_data
        else:
            db_submenu = self.crud.get(submenu_id)
            if db_submenu is None:
                raise HTTPException(
                    status_code=404, detail='submenu not found',
                )
            cached_data = self.cache.set(f'submenu_{submenu_id}', db_submenu)
        return db_submenu

    def create_submenu(
        self,
        menu_id: int,
        submenu: SubmenuCreate,
    ):
        db_submenu = self.crud.get_by_title(title=submenu.title)
        if db_submenu:
            raise HTTPException(
                status_code=400,
                detail='submenu with this title already exist',
            )
        self.cache.delete(f'menu_{menu_id}')
        self.cache.delete('submenu_list')
        self.cache.delete('menu_list')
        return self.crud.create(
            submenu=submenu,
            menu_id=menu_id,
        )

    def update_submenu(
        self, submenu_id: int,
        menu_id: int,
        submenu: SubmenuUpdate,
    ):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        updated_submenu = self.crud.update(
            submenu=submenu,
            submenu_id=submenu_id,
            menu_id=menu_id,
        )
        self.cache.set((f'submenu_{submenu_id}'), updated_submenu)
        self.cache.delete('submenu_list')
        return updated_submenu

    def delete_submenu(
        self, menu_id: int,
        submenu_id: int,
    ):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        self.crud.delete(submenu_id=submenu_id)
        self.cache.delete(f'menu_{menu_id}')
        self.cache.delete(f'submenu_{submenu_id}')
        self.cache.delete('menu_list')
        self.cache.delete('submenu_list')
        self.cache.delete('dish_list')
        return {'status': 'true', 'message': 'The menu has been deleted'}
