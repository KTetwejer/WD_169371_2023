lista = ["Nie", "lubię", "marki", "BMW"]

def dodaj_znak_b(lista):
    lista1 = []
    for i in range(len(lista)):
        lista1.insert(i, lista[i] + "!")
    return lista1

print(dodaj_znak_b(lista))

lista = ["Nie", "lubię", "marki", "BMW"]

def dodaj_znak_a(lista):

    for i in range(0, len(lista)):
        lista[i] = lista[i].replace(lista[i], lista[i] + "!")
    return lista

print(dodaj_znak_a(lista))


