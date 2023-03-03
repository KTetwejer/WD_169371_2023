# zadanie 8
numbers = input("Podaj liczbe: ")
sum = 0
i = 0

for i in range(0, len(numbers)):
    sum += int(numbers[i])
    i+=1
print(sum)