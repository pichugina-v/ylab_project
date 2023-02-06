from typing import Optional

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: Optional[str]


class MenuCreate(MenuBase):
    description: str


class MenuUpdate(MenuBase):
    pass


class MenuInDB(MenuBase):
    class Config:
        orm_mode = True


class MenuGet(MenuInDB):
    submenus_count: int
    dishes_count: int
    description: str
    id: str
