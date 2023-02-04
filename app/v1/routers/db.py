from fastapi import APIRouter, Depends

from ..dependencies import get_db_service
from ..services.db_service import DatabaseService

router = APIRouter()

@router.get(
    '/upload',
    summary='Загрузить тестовые данные в базу данных',
)
async def upload_data(
    db_service: DatabaseService = Depends(get_db_service),
):
    """Загрузить тестовые данные в базу данных"""
    return await db_service.upload_data()