import json

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.models import Dish, Menu, Submenu


class DataTestService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def upload_data(self):
        with open('app/db/db_data.json') as data:
            data = json.load(data)

            menus_amount = len(data['menus'])
            submenus_amount = len(data['submenus'])
            dishes_amount = len(data['dishes'])

            for i in range(1, menus_amount + 1):
                db_menu = Menu(
                    id=data['menus'][f'menu{i}']['id'],
                    title=data['menus'][f'menu{i}']['title'],
                    description=data['menus'][f'menu{i}']['description'],
                )
                self.db.add(db_menu)
                await self.db.commit()
                await self.db.refresh(db_menu)

            for i in range(1, submenus_amount + 1):
                db_submenu = Submenu(
                    id=data['submenus'][f'submenu{i}']['id'],
                    title=data['submenus'][f'submenu{i}']['title'],
                    description=data['submenus'][f'submenu{i}']['description'],
                    menu_id=data['submenus'][f'submenu{i}']['menu_id'],
                )
                self.db.add(db_submenu)
                await self.db.commit()
                await self.db.refresh(db_submenu)

            for i in range(1, dishes_amount + 1):
                db_dish = Dish(
                    id=data['dishes'][f'dish{i}']['id'],
                    title=data['dishes'][f'dish{i}']['title'],
                    description=data['dishes'][f'dish{i}']['description'],
                    submenu_id=data['dishes'][f'dish{i}']['submenu_id'],
                    price=data['dishes'][f'dish{i}']['price'],
                )
                self.db.add(db_dish)
                await self.db.commit()
                await self.db.refresh(db_dish)

        return {'message': 'Data was uploaded successfully'}
