from typing import Optional, Union

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: Optional[str]


class MenuCreate(MenuBase):
    description: str


class MenuUpdate(MenuBase):
    description: Union[str, None] = None


class MenuInDB(MenuBase):

    class Config:
        orm_mode = True


class MenuGet(MenuInDB):
    submenus_count: int
    dishes_count: int
    id: str
