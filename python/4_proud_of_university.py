# Функция make_report_about_top3 принимает словарь (students_avg_scores), в котором ключами являются имена студентов, а значениями — средний балл за всю учебу. Функция находит ТОП-3 студентов, чей средний балл выше, чем у других. Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который потом будет передан в бухгалтерию. Сам файл необходимо создать внутри функции. Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без проблем получить всю нужную информацию. Пример входных данных приведен ниже

import pandas as pd
from itertools import islice

students_avg_scores = {
    'Max': 4.964, 
    'Eric': 4.962, 
    'Peter': 4.923, 
    'Mark': 4.957, 
    'Julie': 4.95, 
    'Jimmy': 4.973, 
    'Felix': 4.937, 
    'Vasya': 4.911, 
    'Don': 4.936, 
    'Zoi': 4.937}

def make_report_about_top3(avg_scores=dict):
    file = 'top_3_students.xlsx'
    avg_scores = dict(sorted(avg_scores.items(), key=lambda item: item[1]))
    top_3 = pd.DataFrame(avg_scores, index = [0])
    
    top_3.to_excel(file)
    # with xlsxwriter.Workbook(file) as workbook:
    #     worksheet = workbook.add_worksheet()
    #     for row_name, data in enumerate(top3):
    #         worksheet.write_row(row_name, 0, data)
    return file

print(make_report_about_top3(students_avg_scores))

