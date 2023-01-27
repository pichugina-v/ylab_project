from typing import List

from fastapi import APIRouter, Depends

from ..dependencies import get_dish_service
from ..services.dish_service import DishService
from ..schemas.dish import DishGet, DishCreate, DishUpdate

router = APIRouter()

@router.get('/dishes', response_model=List[DishGet])
def read_dishes(dish_service: DishService = Depends(get_dish_service)):
    return dish_service.get_dishes()

@router.get("/dishes/{dish_id}", response_model=DishGet)
def read_dish(dish_id: int,
              dish_service: DishService = Depends(get_dish_service)):
    return dish_service.get_dish(dish_id=dish_id)

@router.post("/dishes", response_model=DishGet, status_code=201)
def create_dish(submenu_id: int,
                dish: DishCreate,
                dish_service: DishService = Depends(get_dish_service)):
    return dish_service.create_dish(submenu_id=submenu_id, dish=dish)

@router.patch("/dishes/{dish_id}", response_model=DishGet)
def update_dish(submenu_id: int,
                dish_id: int,
                dish: DishUpdate,
                dish_service: DishService = Depends(get_dish_service)):
    return dish_service.update_dish(submenu_id=submenu_id, dish_id=dish_id, dish=dish)

@router.delete("/dishes/{dish_id}")
def delete_dish(dish_id: int,
                dish_service: DishService = Depends(get_dish_service)):
    return dish_service.delete_dish(dish_id=dish_id)
