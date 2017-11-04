numbers = input("Enter list of numbers:")
print(numbers.split())

def addition(x):
    add = 0

    for i in numbers.split():
        add += int(i)

    return add


def multiplication(x):
    mul = 1
    for i in numbers.split():
        mul *= int(i)

    return mul

print(format(addition(numbers)))
print(format(multiplication(numbers)))

