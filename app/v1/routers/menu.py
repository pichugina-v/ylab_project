from fastapi import APIRouter, Body, Depends

from ..dependencies import get_menu_service
from ..schemas.error_message import Message404, MessageDeleted
from ..schemas.menu import MenuCreate, MenuGet, MenuUpdate
from ..services.menu_service import MenuService

router = APIRouter()


@router.get(
    '/menus',
    response_model=list[MenuGet],
    summary='Получить список меню',
    response_description='Список всех меню',
)
async def read_menus(
    menu_service: MenuService = Depends(get_menu_service),
):
    """Получить список всех меню"""
    return await menu_service.get_menus()


@router.get(
    '/menus/{menu_id}',
    response_model=MenuGet,
    responses={404: {'model': Message404}},
    summary='Получить детальную информацию о меню',
    response_description='Детальная информация о меню',
)
async def read_menu(
    menu_id: int,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Получить детальную информацию о меню"""
    return await menu_service.get_menu(
        menu_id=menu_id,
    )


@router.post(
    '/menus',
    response_model=MenuGet,
    summary='Создать меню',
    response_description='Созданное меню',
    status_code=201,
)
async def create_menu(
    menu: MenuCreate = Body(
        example={
            'title': 'Menu 1',
            'description': 'Menu 1 description',
        },
    ),
    menu_service: MenuService = Depends(get_menu_service),
):
    """Создать меню"""
    return await menu_service.create_menu(menu=menu)


@router.patch(
    '/menus/{menu_id}',
    response_model=MenuGet,
    responses={404: {'model': Message404}},
    summary='Изменить меню',
    response_description='Измененное меню',
)
async def update_menu(
    menu_id: int,
    menu: MenuUpdate = Body(
        example={
            'title': 'Menu 1 updated',
            'description': 'Menu 1 description updated',
        },
    ),
    menu_service: MenuService = Depends(get_menu_service),
):
    """Изменить меню"""
    return await menu_service.update_menu(
        menu_id=menu_id,
        menu=menu,
    )


@router.delete(
    '/menus/{menu_id}',
    responses={404: {'model': Message404}, 200: {'model': MessageDeleted}},
    summary='Удалить меню',
)
async def delete_menu(
    menu_id: int,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Удалить меню"""
    return await menu_service.delete_menu(
        menu_id=menu_id,
    )
