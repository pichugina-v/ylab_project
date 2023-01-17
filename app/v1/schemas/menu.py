from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):
    pass


class MenuInDB(MenuBase):
    id: int

    
    class Config:
        orm_mode = True


class MenuGet(MenuInDB):
    submenus_count: int
    dishes_count: int
    id: str
