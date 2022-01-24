names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]

def get_inductees(students=list, birth_years=list, gender=list):
    inductees, failures = [], []
    for i in range(len(students)):
        if not birth_years[i] and gender[i] == "Male" or not gender[i] and birth_years[i]:
            failures.append([students[i], birth_years[i], gender[i]])
        if gender[i] == "Male":
            if birth_years[i]:
                if 17 < 2021 - birth_years[i] < 30:
                    inductees.append(students[i])
    return inductees, failures

print(get_inductees(names, birthday_years, genders))
