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

import pandas as pd

def make_report_about_top3(avg_scores=dict):
    file = 'top_3_students.xlsx'
    avg_scores = dict(sorted(avg_scores.items(), key=lambda item: item[1], reverse=True))
    top_3 = pd.DataFrame.from_dict(avg_scores, orient='index',columns=None)
    top_3 = top_3[:3]
    top_3.to_excel(file, header=False)
    return file

print(make_report_about_top3(students_avg_scores))

