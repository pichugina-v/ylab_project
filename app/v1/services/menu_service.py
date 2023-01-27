from fastapi import HTTPException

from ..crud.menu_crud import MenuCrud
from ..schemas.menu import MenuCreate, MenuUpdate


class MenuService:
    def __init__(self, crud: MenuCrud):
        self.crud = crud

    def get_menus(self):
        return self.crud.get_list()

    def get_menu(self, menu_id: int):
        db_menu = self.crud.get(menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail="menu not found")
        return db_menu

    def create_menu(self, menu: MenuCreate):
        db_menu = self.crud.get_by_title(title=menu.title)
        if db_menu:
            raise HTTPException(
                status_code=400,
                detail='menu with this title already exist'
            )
        return self.crud.create(menu=menu)

    def update_menu(self, menu_id: int, menu: MenuUpdate):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        return self.crud.update(menu=menu, menu_id=menu_id)
    
    def delete_menu(self, menu_id: int):
        db_menu = self.crud.get(menu_id=menu_id)
        if db_menu is None:
            raise HTTPException(status_code=404, detail='menu not found')
        self.crud.delete(menu_id=menu_id)
        return {'message': 'The menu has been deleted'}
