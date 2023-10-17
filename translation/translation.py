import openpyxl
import json


def load_translations():
    workbook = openpyxl.load_workbook("workbooks/languages.xlsx")
    worksheet = workbook.active
    json_object = {}
    i = 3
    while True:
        if worksheet.cell(row=i, column=2).value is None or worksheet.cell(row=i, column=3).value is None:
            break
        json_object[worksheet.cell(row=i, column=3).value] = worksheet.cell(row=i, column=2).value
        i += 1
    workbook.close()
    file = open("translation/translations.json", "w")
    file.write(json.dumps(json_object))
    file.close()


def translate(name):
    with open("translation/translations.json", "r") as file:
        content = file.read()
        return json.loads(content)[name]
