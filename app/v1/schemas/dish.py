from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    title: str


class DishInDB(DishBase):
    id: int

    
    class Config:
        orm_mode = True


class DishGet(DishInDB):
    pass
