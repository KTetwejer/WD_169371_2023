def funkcja(a1, a2):
    if(a1 == a2 and (a1*a2) != -1):
        return ("Proste są równoległe")

    elif((a1*a2) == -1 and a1 != a2):
        return ("Proste są prostopadłe")

    elif((a1*a2) == -1 and a1 == a2):
        return ("Proste są prostopadłe i równoległe")

    else:
        return ("Prosta ")

a1 = eval(input("Wpisz a1: "))
a2 = eval(input("Wpisz a2: "))
print(funkcja(a1, a2))
