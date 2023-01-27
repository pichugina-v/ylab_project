from typing import List

from fastapi import APIRouter, Depends

from ..dependencies import get_menu_service
from ..services.menu_service import MenuService
from ..schemas.menu import MenuGet, MenuCreate, MenuUpdate

router = APIRouter()

@router.get('/menus', response_model=List[MenuGet])
def read_menus(menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.get_menus()

@router.get('/menus/{menu_id}', response_model=MenuGet)
def read_menu(menu_id: int,
              menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.get_menu(menu_id)

@router.post('/menus', response_model=MenuGet, status_code=201)
def create_menu(menu: MenuCreate,
                menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.create_menu(menu=menu)

@router.patch('/menus/{menu_id}', response_model=MenuGet)
def update_menu(menu_id: int, menu: MenuUpdate,
                menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.update_menu(menu_id=menu_id, menu=menu)

@router.delete('/menus/{menu_id}')
def delete_menu(menu_id: int,
                menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.delete_menu(menu_id=menu_id)
    