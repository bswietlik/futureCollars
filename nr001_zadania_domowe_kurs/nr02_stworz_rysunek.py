#Używajac zagnieżdżonych pętli, stwórz funkcję, która wydrukuje następujcy wzór:

def stworz_rysunek():

    for a in range(0,5):
        for b in range(a+1):
            if b % 2 ==0:
                print('*', end="")
            else:
                print ('$',end="")

        print('')

    for a in range(3,-1,-1):
        for b in range(a+1):
            if b % 2==0:
                print('*', end="")
            else:
                print ('$',end="")
        print('')

    return
print()
stworz_rysunek()
