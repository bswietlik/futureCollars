#Używajac zagnieżdżonych pętli, stwórz funkcję, która wydrukuje następujcy wzór:
def stworz_rysunek():
    n=5;
    for a in range(n):
        for b in range(a):
            print ('*$ ', end="")

        print('')

    for a in range(n,0,-1):
        for b in range(a):
            print('*$ ', end="")
        print('')
    return
stworz_rysunek()
