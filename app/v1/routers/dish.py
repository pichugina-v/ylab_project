from fastapi import APIRouter, Body, Depends, Request

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
def read_dishes(dish_service: DishService = Depends(get_dish_service)):
    """Получить список всех блюд"""
    return dish_service.get_dishes()


@router.get(
    '/dishes/{dish_id}',
    response_model=DishGet,
    responses={404: {'model': Message404}},
    summary='Получить детальную информацию о блюде',
    response_description='Список всех блюд',
)
def read_dish(
    dish_id: int,
    request: Request,
    dish_service: DishService = Depends(get_dish_service),
):
    """Получить детальную информацию о блюде"""
    return dish_service.get_dish(
        dish_id=dish_id,
        url=request.url._url,
    )


@router.post(
    '/dishes',
    response_model=DishGet,
    summary='Создать блюдо',
    response_description='Созданное блюдо',
    status_code=201,
)
def create_dish(
    submenu_id: int,
    request: Request,
    dish: DishCreate = Body(
        example={
            'title': 'Dish 1',
            'description': 'Dish 1 description',
        },
    ),
    dish_service: DishService = Depends(get_dish_service),
):
    """Создать блюдо"""
    return dish_service.create_dish(
        submenu_id=submenu_id,
        url=request.url._url,
        dish=dish,
    )


@router.patch(
    '/dishes/{dish_id}',
    responses={404: {'model': Message404}},
    summary='Изменить блюдо',
    response_description='Измененное блюдо',
    response_model=DishGet,
)
def update_dish(
    submenu_id: int,
    dish_id: int,
    request: Request,
    dish: DishUpdate = Body(
        example={
            'title': 'Dish 1 updated',
            'description': 'Dish 1 description updated',
        },
    ),
    dish_service: DishService = Depends(get_dish_service),
):
    """Изменить блюдо"""
    return dish_service.update_dish(
        submenu_id=submenu_id,
        url=request.url._url,
        dish_id=dish_id,
        dish=dish,
    )


@router.delete(
    '/dishes/{dish_id}',
    responses={404: {'model': Message404}, 200: {'model': MessageDeleted}},
    summary='Удалить блюдо',
)
def delete_dish(
    dish_id: int,
    request: Request,
    dish_service: DishService = Depends(get_dish_service),
):
    """Удалить блюдо"""
    return dish_service.delete_dish(
        dish_id=dish_id,
        url=request.url._url,
    )
