#Napisz funkcje (lambda), ktora z podanej listy liczb wyfiltruje liste liczb parzystych i nieparzystych
lista=[1,2,4,5,18,24,29,32,36,48,57,65,66,80,82,87]
fnp= list(filter(lambda liczba: liczba % 2 == 0, lista))
fnnp= list(filter(lambda liczba:liczba %2 != 0, lista))
print(fnp)
print(fnnp)