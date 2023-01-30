from fastapi import APIRouter, Body, Depends

from ..dependencies import get_submenu_service
from ..schemas.error_message import Message404, MessageDeleted
from ..schemas.submenu import SubmenuCreate, SubmenuGet, SubmenuUpdate
from ..services.submenu_service import SubmenuService

router = APIRouter()


@router.get(
    '/submenus',
    response_model=list[SubmenuGet],
    summary='Получить список подменю',
    response_description='Список всех подменю',
)
def read_submenus(
    submenu_service: SubmenuService = Depends(
        get_submenu_service,
    ),
):
    """Получить список всех подменю"""
    return submenu_service.get_submenus()


@router.get(
    '/submenus/{submenu_id}',
    responses={404: {'model': Message404}},
    response_model=SubmenuGet,
    summary='Получить детальную информацию о подменю',
    response_description='Детальная информация о подменю',
)
def read_submenu(
    submenu_id: int,
    submenu_service: SubmenuService = Depends(
        get_submenu_service,
    ),
):
    """Получить детальную информацию о подменю"""
    return submenu_service.get_submenu(
        submenu_id=submenu_id,
    )


@router.post(
    '/submenus',
    response_model=SubmenuGet,
    summary='Создать подменю',
    response_description='Созданное подменю',
    status_code=201,
)
def create_submenu(
    menu_id: int,
    submenu: SubmenuCreate = Body(
        example={
            'title': 'Submenu 1',
            'description': 'Submenu 1 description',
        },
    ),
    submenu_service: SubmenuService = Depends(
        get_submenu_service,
    ),
):
    """Создать подменю"""
    return submenu_service.create_submenu(
        menu_id=menu_id,
        submenu=submenu,
    )


@router.patch(
    '/submenus/{submenu_id}',
    responses={404: {'model': Message404}},
    response_model=SubmenuGet,
    summary='Обновить подменю',
    response_description='Обновленное подменю',
)
def update_submenu(
    menu_id: int,
    submenu_id: int,
    submenu: SubmenuUpdate = Body(
        example={
            'title': 'Submenu 1 updated',
            'description': 'Submenu 1 description updated',
        },
    ),
    submenu_service: SubmenuService = Depends(
        get_submenu_service,
    ),
):
    """Обновить подменю"""
    return submenu_service.update_submenu(
        menu_id=menu_id,
        submenu_id=submenu_id,
        submenu=submenu,
    )


@router.delete(
    '/submenus/{submenu_id}',
    responses={404: {'model': Message404}, 200: {'model': MessageDeleted}},
    summary='Удалить подменю',
)
def delete_submenu(
    menu_id: int,
    submenu_id: int,
    submenu_service: SubmenuService = Depends(
        get_submenu_service,
    ),
):
    """Удалить подменю"""
    return submenu_service.delete_submenu(
        menu_id=menu_id,
        submenu_id=submenu_id,
    )
