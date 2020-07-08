#5. Napisz funkcje, ktora przyjmuje string i zwraca liczbe malych oraz wielkich liter.
def SprawdzWielkoscLiter(napis):
    wynik_malych=0
    wynik_duzych=0
    for i in napis:
        if i.islower():
            wynik_malych+=1
        elif i.isupper() and not i.isspace():
            wynik_duzych+=1
    return (wynik_malych, wynik_duzych)
napis=('BeAtKa Ma PsA')
print(SprawdzWielkoscLiter(napis))