from fastapi import APIRouter, Body, Depends

from ..dependencies import get_dish_service
from ..schemas.dish import DishCreate, DishGet, DishUpdate
from ..schemas.error_message import Message404, MessageDeleted
from ..services.dish_service import DishService

router = APIRouter()


@router.get(
    '/dishes',
    response_model=list[DishGet],
    summary='Получить список блюд',
    response_description='Список всех блюд',
)
async def read_dishes(
    dish_service: DishService = Depends(get_dish_service),
):
    """Получить список всех блюд"""
    return await dish_service.get_dishes()


@router.get(
    '/dishes/{dish_id}',
    response_model=DishGet,
    responses={404: {'model': Message404}},
    summary='Получить детальную информацию о блюде',
    response_description='Список всех блюд',
)
async def read_dish(
    dish_id: int,
    dish_service: DishService = Depends(get_dish_service),
):
    """Получить детальную информацию о блюде"""
    return await dish_service.get_dish(
        dish_id=dish_id,
    )


@router.post(
    '/dishes',
    response_model=DishGet,
    summary='Создать блюдо',
    response_description='Созданное блюдо',
    status_code=201,
)
async def create_dish(
    menu_id: int,
    submenu_id: int,
    dish: DishCreate = Body(
        example={
            'title': 'Dish 1',
            'description': 'Dish 1 description',
        },
    ),
    dish_service: DishService = Depends(get_dish_service),
):
    """Создать блюдо"""
    return await dish_service.create_dish(
        menu_id=menu_id,
        submenu_id=submenu_id,
        dish=dish,
    )


@router.patch(
    '/dishes/{dish_id}',
    responses={404: {'model': Message404}},
    summary='Изменить блюдо',
    response_description='Измененное блюдо',
    response_model=DishGet,
)
async def update_dish(
    dish_id: int,
    dish: DishUpdate = Body(
        example={
            'title': 'Dish 1 updated',
            'description': 'Dish 1 description updated',
        },
    ),
    dish_service: DishService = Depends(get_dish_service),
):
    """Изменить блюдо"""
    return await dish_service.update_dish(
        dish_id=dish_id,
        dish=dish,
    )


@router.delete(
    '/dishes/{dish_id}',
    responses={404: {'model': Message404}, 200: {'model': MessageDeleted}},
    summary='Удалить блюдо',
)
async def delete_dish(
    menu_id: int,
    submenu_id: int,
    dish_id: int,
    dish_service: DishService = Depends(get_dish_service),
):
    """Удалить блюдо"""
    return await dish_service.delete_dish(
        menu_id=menu_id,
        submenu_id=submenu_id,
        dish_id=dish_id,
    )
