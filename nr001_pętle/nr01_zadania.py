# znajdz liczby , które można podzielić przez 7 i wielokrotnosc liczby 5 w przedziale 1500 a 2700

# for i in range(1500, 2701):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#

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
ktoreUrodziny([1954, 1986, 1990, 1998])


