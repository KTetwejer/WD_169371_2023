# zadanie 1
zdanie = input("Wpisz zdanie: ")
length = len(zdanie)
i = 0
counter = 0
while i < length:
    if zdanie[i] == " ":
        i+=1
        counter+=1
    else:
        i+=1
print(counter)
