numbers = input("Enter list of numbers:")
#print(numbers)

addition = 0
multiplication = 1

for i in numbers.split():
    addition = addition + int(i)
    multiplication *= int(i)

print(addition)
print(multiplication)

