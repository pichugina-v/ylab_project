from sqlalchemy.future import select
from sqlalchemy.orm import Session

from ..models.models import Submenu
from ..schemas.submenu import SubmenuCreate, SubmenuUpdate


class SubmenuCrud:
    def __init__(self, db: Session):
        self.db = db

    async def get(self, submenu_id: int):
        db_submenu = await self.db.get(Submenu, submenu_id)
        if db_submenu is None:
            return None
        return db_submenu

    async def get_by_title(self, title: str):
        db_submenu = (
            await self.db.execute(
                select(Submenu).where(Submenu.title == title),
            )
        ).scalars().first()
        if db_submenu is None:
            return None
        return db_submenu

    async def get_list(self):
        db_submenus = (
            await self.db.execute(select(Submenu))
        ).scalars().fetchall()
        return db_submenus

    async def create(self, menu_id: int, submenu: SubmenuCreate):
        new_submenu = Submenu(
            title=submenu.title,
            description=submenu.description,
            menu_id=menu_id,
        )
        self.db.add(new_submenu)
        await self.db.commit()
        await self.db.refresh(new_submenu)
        return new_submenu

    async def update(self, submenu_id: int, menu_id: int, submenu: SubmenuUpdate):
        db_submenu = await self.db.get(Submenu, submenu_id)
        submenu_data = submenu.dict(exclude_unset=True)
        for key, value in submenu_data.items():
            setattr(db_submenu, key, value)
        await self.db.commit()
        await self.db.refresh(db_submenu)
        return db_submenu

    async def delete(self, submenu_id: int):
        db_submenu = await self.db.get(Submenu, submenu_id)
        await self.db.delete(db_submenu)
        await self.db.commit()
