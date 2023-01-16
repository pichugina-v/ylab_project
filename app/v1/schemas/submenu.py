from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreate(SubmenuBase):
    pass


class SubmenuUpdate(SubmenuBase):
    title: str


class SubmenuInDB(BaseModel):
    id: int

    
    class Config:
        orm_mode = True


class SubmenuGet(SubmenuInDB):
    dishes_count: int
