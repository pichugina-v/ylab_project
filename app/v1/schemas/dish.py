from typing import Optional

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: Optional[str]
    price: Optional[str]


class DishCreate(DishBase):
    description: str
    price: str


class DishUpdate(DishBase):
    pass


class DishInDB(DishBase):
    class Config:
        orm_mode = True


class DishGet(DishInDB):
    id: str
    description: str
    price: str
