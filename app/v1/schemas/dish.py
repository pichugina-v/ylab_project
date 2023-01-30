from typing import Optional, Union

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: Optional[str]
    price: Optional[str]


class DishCreate(DishBase):
    description: str
    price: str


class DishUpdate(DishBase):
    description: Union[str, None] = None
    price: Union[str, None] = None


class DishInDB(DishBase):

    class Config:
        orm_mode = True


class DishGet(DishInDB):
    id: str
