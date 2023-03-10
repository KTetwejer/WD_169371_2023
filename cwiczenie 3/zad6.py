import random


def guess_the_number():
    suma = 0
    random.seed()
    b = random.randint(1, 10)
    for i in range(0, 5):
        a = eval(input("Zgadnij liczbę: "))
        if (a in range(1, 10)):
            if (a == b):
                suma += 10
                print("Zgadłeś!")
            else:
                suma -= 1
                print("Nie zgadłeś :c")
    return suma
print(guess_the_number())