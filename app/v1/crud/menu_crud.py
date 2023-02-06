from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models.models import Menu
from ..schemas.menu import MenuCreate, MenuUpdate


class MenuCrud:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, menu_id: int):
        db_menu = await self.db.get(Menu, menu_id)
        if db_menu is None:
            return None
        return db_menu

    async def get_by_title(self, title: str):
        db_menu = (
            (
                await self.db.execute(
                    select(Menu).where(Menu.title == title),
                )
            )
            .scalars()
            .first()
        )
        if not db_menu:
            return None
        return db_menu

    async def get_list(self):
        db_menus = (await self.db.execute(select(Menu))).scalars().fetchall()
        return db_menus

    async def create(self, menu: MenuCreate):
        new_menu = Menu(title=menu.title, description=menu.description)
        self.db.add(new_menu)
        await self.db.commit()
        await self.db.refresh(new_menu)
        return new_menu

    async def update(self, menu_id: int, menu: MenuUpdate):
        db_menu = await self.db.get(Menu, menu_id)
        menu_data = menu.dict(exclude_unset=True)
        for key, value in menu_data.items():
            setattr(db_menu, key, value)
        await self.db.commit()
        await self.db.refresh(db_menu)
        return db_menu

    async def delete(self, menu_id: int):
        db_menu = await self.db.get(Menu, menu_id)
        await self.db.delete(db_menu)
        await self.db.commit()
