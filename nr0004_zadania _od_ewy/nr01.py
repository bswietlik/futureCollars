#Napisz program, który zwróci liczby, które beda podzielne przez 7 oraz beda wielokrotnoscia 5 pomiedzy 1500 a 2700 (uwzględniając obie liczby)
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

list = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]
print(list)