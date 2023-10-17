import openpyxl


def save_cell(filename, worksheet_name, cell, data):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook[worksheet_name]
    worksheet[cell] = data
    workbook.save(filename)
