from typing import List

from fastapi import APIRouter, Depends

from ..dependencies import get_submenu_service
from ..services.submenu_service import SubmenuService
from ..schemas.submenu import SubmenuGet, SubmenuCreate, SubmenuUpdate

router = APIRouter()

@router.get('/submenus', response_model=List[SubmenuGet])
def read_submenus(submenu_service: SubmenuService = Depends(get_submenu_service)):
    return submenu_service.get_submenus()

@router.get("/submenus/{submenu_id}", response_model=SubmenuGet)
def read_submenu(submenu_id: int,
                 submenu_service: SubmenuService = Depends(get_submenu_service)):
    return submenu_service.get_submenu(submenu_id=submenu_id)

@router.post("/submenus", response_model=SubmenuGet, status_code=201)
def create_submenu(menu_id: int,
                   submenu: SubmenuCreate,
                   submenu_service: SubmenuService = Depends(get_submenu_service)):
    return submenu_service.create_submenu(menu_id=menu_id, submenu=submenu)

@router.patch("/submenus/{submenu_id}", response_model=SubmenuGet)
def update_submenu(menu_id: int,
                   submenu_id: int,
                   submenu: SubmenuUpdate,
                   submenu_service: SubmenuService = Depends(get_submenu_service)):
    return submenu_service.update_submenu(menu_id=menu_id, submenu_id=submenu_id, submenu=submenu)

@router.delete("/submenus/{submenu_id}")
def delete_submenu(submenu_id: int,
                   submenu_service: SubmenuService = Depends(get_submenu_service)):
    return submenu_service.delete_submenu(submenu_id=submenu_id)
    