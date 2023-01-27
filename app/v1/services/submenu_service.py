from fastapi import HTTPException

from ..crud.submenu_crud import SubmenuCrud
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate


class SubmenuService:
    def __init__(self, crud: SubmenuCrud):
        self.crud = crud

    def get_submenus(self):
        return self.crud.get_list()

    def get_submenu(self, submenu_id: int):
        db_submenu = self.crud.get(submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail="submenu not found")
        return db_submenu

    def create_submenu(self, menu_id: int, submenu: SubmenuCreate):
        db_submenu = self.crud.get_by_title(title=submenu.title)
        if db_submenu:
            raise HTTPException(
                status_code=400,
                detail='submenu with this title already exist'
            )
        return self.crud.create(submenu=submenu, menu_id=menu_id)

    def update_submenu(self, submenu_id: int, menu_id: int, submenu: SubmenuUpdate):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        return self.crud.update(submenu=submenu, submenu_id=submenu_id, menu_id=menu_id)
    
    def delete_submenu(self, submenu_id: int):
        db_submenu = self.crud.get(submenu_id=submenu_id)
        if db_submenu is None:
            raise HTTPException(status_code=404, detail='submenu not found')
        self.crud.delete(submenu_id=submenu_id)
        return {'message': 'The submenu has been deleted'}
