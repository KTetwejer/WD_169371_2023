import math

def funkcja(a = 3, b = 4):
    c = math.sqrt((a * a) + (b * b))
    return c

a = eval(input("Podaj a: "))
b = eval(input("Podaj b: "))
print(f"C = {funkcja(a, b)}")
