from pytest import fixture
from app.v1.models.models import Dish

@fixture()
def dish_1(db, submenu_1):
    title = 'New dish 1'
    description = 'New dish 1 description'
    price = '12.50'
    new_dish = Dish(
        title=title,
        description=description,
        price=price,
        submenu_id=submenu_1.id
    )
    db.add(new_dish)
    db.commit()

    return Dish(
        id=new_dish.id,
        title=title,
        description=description,
        price=price
    )

@fixture()
def dish_2(db, submenu_1):
    title = 'New dish 2'
    description = 'New dish 2 description'
    price = '12.50'
    new_dish = Dish(
        title=title,
        description=description,
        price=price,
        submenu_id=submenu_1.id
    )
    db.add(new_dish)
    db.commit()

    return Dish(
        id=new_dish.id,
        title=title,
        description=description,
        price=price
    )