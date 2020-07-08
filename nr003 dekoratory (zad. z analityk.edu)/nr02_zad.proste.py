def zwykłaFunkcja(): #funkcja tylko drukuje napis
    print("To jest zwykła funkcja")


def dekor(funkcja):  #Rolą tej funkcji, jest ‚udekowowanie’ przekazane mu w parametrze funkcje.
    def wew():  #Funkcja ‚Dekor’, tworzy funkcję wewnętrzną ‚wew()’, która
        print("Dekorujemy funkcję")  #wykonuje ‚dekorację’, czyli w naszym przypadku, dodaje swój napis,
        return funkcja() #wywołuje funkcję, przekazaną w parametrze do ‚dekor’

    return wew


nowaFunkcja = dekor(zwykłaFunkcja) #wywołujemy funkcję ‚dekor’, przekazujemy w parametrze funkcję ‚zwykłaFunkcja’
nowaFunkcja()


# z użyciem @dekor

def dekor(funkcja): #definiujemy funkcję dekoratora
    def wew():
        print("Dekorujemy funkcję")
        return funkcja()

    return wew


@dekor
def zwykłaFunkcja():
    print("To jest zwykła funkcja")

nowaFunkcja()

#przykład 3

def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcję")
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwykłaFunkcja(a, b, c):
    print("To jest zwykła funkcja, która dodaje liczby:")
    print(a + b + c)


zwykłaFunkcja(1, 2, 3)