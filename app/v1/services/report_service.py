from celery.result import AsyncResult
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..celery.tasks import form_excel
from ..models.models import Dish, Menu, Submenu


class ReportService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def extract_data_from_db(self):
        dish_subq = (
            select(
                Dish.submenu_id,
                func.json_agg(
                    func.json_build_object(
                        'title',
                        Dish.title,
                        'description',
                        Dish.description,
                        'price',
                        Dish.price,
                    ),
                ).label('dishes'),
            )
            .select_from(
                Dish,
            )
            .group_by(
                Dish.submenu_id,
            )
            .subquery()
        )

        submenu_subq = (
            select(
                Submenu.menu_id,
                func.json_agg(
                    func.json_build_object(
                        'title',
                        Submenu.title,
                        'description',
                        Submenu.description,
                        'dishes',
                        dish_subq.c.dishes,
                    ),
                ).label('submenus'),
            )
            .select_from(
                Submenu,
            )
            .group_by(
                Submenu.menu_id,
            )
            .join(
                dish_subq,
                dish_subq.c.submenu_id == Submenu.id,
            )
            .subquery()
        )

        query = (
            select(
                Menu.title,
                Menu.description,
                submenu_subq.c.submenus,
            )
            .select_from(
                Menu,
            )
            .join(
                submenu_subq,
                submenu_subq.c.menu_id == Menu.id,
            )
        )

        db_data = await self.db.execute(query)
        data = [dict(data) for data in db_data]
        task_id = form_excel.delay(data)
        return task_id

    def check_task_state(self, task_id):
        task = AsyncResult(str(task_id))
        return {
            'task_id': str(task_id),
            'state': str(task.state),
        }
