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