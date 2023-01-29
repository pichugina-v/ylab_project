from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreate(SubmenuBase):
    pass


class SubmenuUpdate(SubmenuBase):
    pass


class SubmenuInDB(SubmenuBase):

    class Config:
        orm_mode = True


class SubmenuGet(SubmenuInDB):
    dishes_count: int
    id: str
