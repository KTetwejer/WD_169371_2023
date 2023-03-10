def monotonicznosc(a):
    if(a > 0):
        return ("Funkcja rosnąca ")
    elif(a < 0):
        return ("Funkcja malejąca")
    else:
        return ("Funkcja stała" )

a = eval(input("Podaj wartosc a: "))
print(monotonicznosc(a))