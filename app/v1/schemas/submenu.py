from typing import Optional, Union

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: Optional[str]


class SubmenuCreate(SubmenuBase):
    description: str


class SubmenuUpdate(SubmenuBase):
    description: Union[str, None] = None


class SubmenuInDB(SubmenuBase):

    class Config:
        orm_mode = True


class SubmenuGet(SubmenuInDB):
    dishes_count: int
    id: str
