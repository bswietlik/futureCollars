#Stwórz klasę reprezentujaca wielokat, i przyjmujaca w konstruktorze listę kolejnych linii (obiekty klasy z poprzedniego zadania),
# reprezentujacych kolejne boki wielokata. Klasa powinna sprawdzic czy dane sa poprawne (czy każda linia kończy się tam gdzie zaczyna następna).
# Klasa wielokata implementuje również metodę obliczajaca obwód.

class Wielokat:
    def __init__(self, a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def oblicz_obwod(self):
        print("obwód wynosi:" ,int(self.a+self.b+self.c+self.d))

figura=Wielokat(4,4,4,4)
figura.oblicz_obwod()