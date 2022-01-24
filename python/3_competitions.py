# Функция find_athlets принимает 3 списка с именами студентов. В первом списке (know_english) — список тех, кто хорошо владеет английским языком. Второй (sportsmen) — содержит имена тех, кто увлекается спортом. Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет. Функция возвращает список имен студентов, которые подходят под все три критерия. Пример входных данных приведен ниже.

know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(who_knows_english=list,who_sport=list,who_older_20=list):
    talents = []
    for speaker in who_knows_english:
        if speaker in who_sport and speaker in who_older_20:
            talents.append(speaker)
    return talents

print(find_athlets(know_english, sportsmen, more_than_20_years))