from sqlalchemy.future import select
from sqlalchemy.orm import Session

from ..models.models import Dish
from ..schemas.dish import DishCreate, DishUpdate


class DishCrud:
    def __init__(self, db: Session):
        self.db = db

    async def get(self, dish_id: int):
        db_dish = await self.db.get(Dish, dish_id)
        if db_dish is None:
            return None
        return db_dish

    async def get_by_title(self, title: str):
        db_dish = (
            await self.db.execute(
                select(Dish).where(Dish.title == title),
            )
        ).scalars().first()
        if db_dish is None:
            return None
        return db_dish

    async def get_list(self):
        db_dishes = (
            await self.db.execute(select(Dish))
        ).scalars().fetchall()
        return db_dishes

    async def create(self, submenu_id: int, dish: DishCreate):
        db_dish = Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            submenu_id=submenu_id,
        )
        self.db.add(db_dish)
        await self.db.commit()
        await self.db.refresh(db_dish)
        return db_dish

    async def update(self, dish_id: int, dish: DishUpdate):
        db_dish = await self.db.get(Dish, dish_id)
        dish_data = dish.dict(exclude_unset=True)
        for key, value in dish_data.items():
            setattr(db_dish, key, value)
        await self.db.commit()
        await self.db.refresh(db_dish)
        return db_dish

    async def delete(self, dish_id: int):
        db_dish = await self.db.get(Dish, dish_id)
        await self.db.delete(db_dish)
        await self.db.commit()
