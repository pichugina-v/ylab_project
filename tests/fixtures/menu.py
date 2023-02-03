from pytest_asyncio import fixture

from app.v1.models.models import Menu


@fixture()
async def menu_1(db):
    title = 'New menu 1'
    description = 'New menu 1 description'
    new_menu = Menu(title=title, description=description)
    db.add(new_menu)
    await db.commit()
    await db.refresh(new_menu)

    return Menu(
        id=new_menu.id,
        title=title,
        description=description,
        dishes_count=new_menu.dishes_count,
        submenus_count=new_menu.submenus_count,
    )
