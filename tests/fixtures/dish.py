from pytest_asyncio import fixture

from app.v1.models.models import Dish


@fixture()
async def dish_1(db, submenu_1):
    title = 'New dish 1'
    description = 'New dish 1 description'
    price = '12.50'
    new_dish = Dish(
        title=title,
        description=description,
        price=price,
        submenu_id=submenu_1.id,
    )
    db.add(new_dish)
    await db.commit()
    await db.refresh(new_dish)

    return Dish(
        id=new_dish.id,
        title=title,
        description=description,
        price=price,
    )
