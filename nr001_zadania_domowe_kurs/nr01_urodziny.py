

# 2 Napisz funkcję, która zwróci które urodziny będą obchodziły w tym roku osoby urodzone w latach
# podanych w lisćie będącej argumentem wejściowym danej funkcji.
def ktoreUrodziny(rok):
    from datetime import date
    day=date.today()
    year=day.year
    roznice=[]
    for wiek in rok:
        roznica=year-wiek
        roznice.append(roznica)
    return roznice

print(ktoreUrodziny([1954, 1986, 1990, 1998]))


