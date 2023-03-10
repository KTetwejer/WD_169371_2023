def funkcja1(a = 1, r = 1, ile = 10):
    i = 0
    suma = 0
    while(i < ile):
        suma += a + (r * i)
        i += 1
    return suma


a = eval(input("Wpisz wartość początkową: "))
b = eval(input("Wpisz różnicę między elementami: "))
c = eval(input("Wpisz ile elementów sumujemy: "))
print("Suma tego ciągu arytmetycznego to ", funkcja1(a, b, c))



