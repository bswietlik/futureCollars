#Stwórz abstrakcyjna klasę bazowa reperzentujaca zwierze. Konstruktor klasy będzie przyjmowac parametr reprezentujacy imię zwierzęcia.
# Klasa będzie miec 2 metody. Jedna metoda daj_glos będzie abstrakcyjna. Druga metoda powitanie będzie wyswietlac napis, składajacy się z wartosci zwracanej
# przez daj_glos, z wyswietlenia imienia zwierzęcia oraz z wyswietlenia jakiego typu (atrybut typ dla klasy) jest zwierze.

from abc import ABC, abstractmethod
class Zwierze(ABC):

    def __init__(self, imie):
        self.imie = imie

    @abstractmethod
    def daj_glos(self):

        def powitanie(self):

            pass

class Kot(Zwierze):
    def __init__(self,odglos,imie,typ):
        super().__init__('Kot')
        self.odglos=odglos
        self.imie=imie
        self.typ=typ

    def daj_glos(self):
        print(self.odglos)
    def powitanie(self):
        print("głośno miałczę",self.odglos, "mam na imie:", self.imie, "jestem z rodziny:", self.typ )

class Pies(Zwierze):
    def __init__(self,odglos,imie,typ):
        super().__init__('Pies')
        self.odglos=odglos
        self.imie=imie
        self.typ=typ

    def daj_glos(self):
        print(self.odglos)
    def powitanie(self):
        print("szczekam:",self.odglos, "wabię się:", self.imie, "jestem typem:", self.typ )

k=Kot("miau miau", "Koteł", "persów")
p=Pies("hau hau", "Pieseł", "pies myśliwski")
k.daj_glos()
p.daj_glos()
k.powitanie()
p.powitanie()




