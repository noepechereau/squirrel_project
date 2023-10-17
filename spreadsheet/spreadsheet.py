import json

import openpyxl


def save_cell(filename, worksheet_name, cell, data):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook[worksheet_name]
    worksheet[cell] = data
    workbook.save(filename)


def workbook_to_json(filename, n):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active
    json_object = {}
    for i in range(3, n + 1):
        json_object[worksheet.cell(row=i, column=2).value] = worksheet.cell(row=i, column=3).value
    workbook.close()
    file = open("resources/translations.json", "w")
    file.write(json.dumps(json_object))
    file.close()
