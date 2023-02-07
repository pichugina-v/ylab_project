from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from ..dependencies import get_report_service, get_test_data_service
from ..schemas.data import DataTestDetail, TaskDetail
from ..services.report_service import ReportService
from ..services.test_data_service import DataTestService

router = APIRouter()

TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


@router.get(
    '/upload',
    summary='Загрузить тестовые данные в базу данных',
    status_code=201,
    responses={201: {'model': DataTestDetail}},
)
async def upload_data(
    test_data_service: DataTestService = Depends(get_test_data_service),
):
    """Загрузить тестовые данные в базу данных"""
    return await test_data_service.upload_data()


@router.post(
    '/request',
    summary='Запросить данные из базы данных в формате .xlsx',
    response_description='Task_id и статус выполнения задания',
    status_code=202,
    responses={202: {'model': TaskDetail}},
)
async def request_excel(
    report_service: ReportService = Depends(get_report_service),
):
    """Запросить данные из базы данных в формате .xlsx"""
    task_id = await report_service.extract_data_from_db()
    return report_service.check_task_state(task_id=task_id)


@router.get(
    '/get/{task_id}',
    summary='Получить данные из базы данных в формате .xlsх',
    response_description='Отчет в формате .xlsx или статус выполнения задания',
)
async def get_excel(
    task_id: str,
    report_service: ReportService = Depends(get_report_service),
):
    """Получить данные из базы данных в формате .xlsх"""
    task_info = report_service.check_task_state(task_id=task_id)
    if task_info['state'] == 'SUCCESS':
        file_name = f'{task_id}.xlsx'
        return FileResponse(
            f'./reports/{task_id}.xlsx',
            media_type=TYPE,
            filename=file_name,
        )
    task_info['message'] = 'The file is preparing'
    return task_info
