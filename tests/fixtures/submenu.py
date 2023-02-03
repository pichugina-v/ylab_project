from pytest_asyncio import fixture

from app.v1.models.models import Submenu


@fixture()
async def submenu_1(db, menu_1):
    title = 'New submenu 1'
    description = 'New submenu 1 description'
    new_submenu = Submenu(
        title=title,
        description=description,
        menu_id=menu_1.id,
    )
    db.add(new_submenu)
    await db.commit()
    await db.refresh(new_submenu)

    return Submenu(
        id=new_submenu.id,
        title=title,
        description=description,
        dishes_count=new_submenu.dishes_count,
    )
