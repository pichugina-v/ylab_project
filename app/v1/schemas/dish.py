from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    pass


class DishInDB(DishBase):
    id: int

    
    class Config:
        orm_mode = True


class DishGet(DishInDB):
    id: str
