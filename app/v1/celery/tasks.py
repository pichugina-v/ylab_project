import xlwt

from .celery import celery


@celery.task
def form_excel(extracted_data):
    task_id = celery.current_task.request.id
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Menus')

    idx = 0
    num1 = 1
    for data in extracted_data:
        sheet.write(idx, 0, num1)
        sheet.write(idx, 1, data['title'])
        sheet.write(idx, 2, data['description'])
        idx += 1
        num2 = 1

        for submenu in data['submenus']:
            sheet.write(idx, 1, num2)
            sheet.write(idx, 2, submenu['title'])
            sheet.write(idx, 3, submenu['description'])
            num2 += 1
            idx += 1
            num3 = 1

            for dish in submenu['dishes']:
                sheet.write(idx, 2, num3)
                sheet.write(idx, 3, dish['title'])
                sheet.write(idx, 4, dish['description'])
                sheet.write(idx, 5, dish['price'])
                num3 += 1
                idx += 1

    workbook.save(f'./reports/{task_id}.xlsx')
    return task_id
