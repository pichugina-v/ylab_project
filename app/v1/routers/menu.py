from fastapi import APIRouter, Depends, Request

from ..dependencies import get_menu_service
from ..schemas.menu import MenuCreate, MenuGet, MenuUpdate
from ..services.menu_service import MenuService

router = APIRouter()


@router.get(
    '/menus', response_model=list[MenuGet],
    summary='Получить список меню',
    response_description='Список всех меню',
)
def read_menus(menu_service: MenuService = Depends(get_menu_service)):
    """Получить список всех меню"""
    return menu_service.get_menus()


@router.get(
    '/menus/{menu_id}', response_model=MenuGet,
    summary='Получить детальную информацию о меню',
    response_description='Детальная информация о меню',
)
def read_menu(
    menu_id: int,
    request: Request,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Получить детальную информацию о меню"""
    return menu_service.get_menu(
        menu_id=menu_id,
        url=request.url._url,
    )


@router.post(
    '/menus', response_model=MenuGet,
    summary='Создать меню',
    response_description='Созданное меню',
    status_code=201,
)
def create_menu(
    menu: MenuCreate,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Создать меню"""
    return menu_service.create_menu(menu=menu)


@router.patch(
    '/menus/{menu_id}', response_model=MenuGet,
    summary='Изменить меню',
    response_description='Измененное меню',
)
def update_menu(
    menu_id: int,
    request: Request,
    menu: MenuUpdate,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Изменить меню"""
    return menu_service.update_menu(
        menu_id=menu_id,
        url=request.url._url,
        menu=menu,
    )


@router.delete(
    '/menus/{menu_id}',
    summary='Удалить меню',
)
def delete_menu(
    menu_id: int,
    request: Request,
    menu_service: MenuService = Depends(get_menu_service),
):
    """Удалить меню"""
    return menu_service.delete_menu(
        menu_id=menu_id,
        url=request.url._url,
    )
