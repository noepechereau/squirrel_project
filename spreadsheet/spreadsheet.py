import openpyxl


def save_cell(filename, worksheet_name, cell, data):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook[worksheet_name]
    worksheet[cell] = data
    workbook.save(filename)


def write_xlsx(data):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['League', 'Golden', 'Other', 'Golden odd', 'other Odd', 'Golden winning chances', 'Other winning '
                                                                                                    'chances'])
    for row in data:
        sheet.append(row)
    workbook.save('workbooks/matches.xlsx')
