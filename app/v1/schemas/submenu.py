from typing import Optional

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: Optional[str]


class SubmenuCreate(SubmenuBase):
    description: str


class SubmenuUpdate(SubmenuBase):
    pass


class SubmenuInDB(SubmenuBase):

    class Config:
        orm_mode = True


class SubmenuGet(SubmenuInDB):
    dishes_count: int
    description: str
    id: str
