# zadanie 5
a = eval(input("Podaj a: "))
b = eval(input("Podaj b: "))
c = eval(input("Podaj c: "))

if a > 0 and a <= 10:
    if a > b or b > c:
        print("Warunki spelnione")
    else:
        print("Jeden warunek spelniony")
else:
    print("Warunki niespelnione")