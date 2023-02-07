import xlwt

from .celery import celery


@celery.task
def form_excel(extracted_data):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Menus')
    style = xlwt.easyxf('font: bold on')

    row: int = 0
    menu_serial_num: int = 1

    for data in extracted_data:
        sheet.write(row, 0, menu_serial_num, style)
        sheet.write(row, 1, data['title'], style)
        sheet.write(row, 2, data['description'], style)
        row += 1

        submenu_serial_num: int = 1
        for submenu in data['submenus']:
            sheet.write(row, 1, submenu_serial_num, style)
            sheet.write(row, 2, submenu['title'], style)
            sheet.write(row, 3, submenu['description'], style)
            submenu_serial_num += 1
            row += 1

            dish_serial_num: int = 1
            for dish in submenu['dishes']:
                sheet.write(row, 2, dish_serial_num, style)
                sheet.write(row, 3, dish['title'], style)
                sheet.write(row, 4, dish['description'], style)
                sheet.write(row, 5, dish['price'], style)
                dish_serial_num += 1
                row += 1

    task_id = celery.current_task.request.id
    workbook.save(f'./reports/{task_id}.xlsx')
    return task_id
