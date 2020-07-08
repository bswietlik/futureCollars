#Napisz program, ktory policzy liczby parzyste i nieparzyste w podanym zbiorze liczb
liczby={1,2,4,5,18,24,29,32,36,48,57,65,66,80,82,87}
parzyste={i for i in liczby if i% 2==0}
nieparzyste={i for i in liczby if i%2!=0}
print(len(parzyste))
print(len(nieparzyste))