from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from ..crud.submenu_crud import SubmenuCrud
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate
from .cache_service import CacheService


class SubmenuService:
    def __init__(self, crud: SubmenuCrud, cache: CacheService):
        self.crud = crud
        self.cache = cache

    def get_submenus(self):
        return self.crud.get_list()

    def get_submenu(self, submenu_id: int, url):
        cached_data = self.cache.get(url)
        if cached_data:
            db_submenu = cached_data
        else:
            db_submenu = self.crud.get(submenu_id)
            if db_submenu is None:
                raise HTTPException(
                    status_code=404, detail='submenu not found',
                )
            cached_data = self.cache.set(url, jsonable_encoder(db_submenu))
        return db_submenu

    def create_submenu(self, menu_id: int, url, submenu: SubmenuCreate):
        db_submenu = self.crud.get_by_title(title=submenu.title)
        if db_submenu:
            raise HTTPException(
                status_code=400,
                detail='submenu with this title already exist',
            )
        self.cache.set_submenus_to_menu(url)
        return self.crud.create(
            submenu=submenu,
            menu_id=menu_id,
        )

    def update_submenu(
        self, submenu_id: int,
        menu_id: int, url, submenu: SubmenuUpdate,
    ):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        self.cache.delete(jsonable_encoder(url))
        return self.crud.update(
            submenu=submenu,
            submenu_id=submenu_id,
            menu_id=menu_id,
        )

    def delete_submenu(self, submenu_id: int, url):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        self.crud.delete(submenu_id=submenu_id)
        self.cache.delete_menu_cache(url)
        self.cache.delete(jsonable_encoder(url))
        return {'status': 'true', 'message': 'The menu has been deleted'}
