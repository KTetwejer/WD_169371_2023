def digital_root(number):
    while len(str(number)) > 1:
        sum = 0
        digits = list(str(number))
        for digit in digits:
            sum += int(digit)
        number = sum

    return number

a = eval(input("Podaj liczbę: "))
print(digital_root(a))