a = int(input("enter first number:"))
b = int(input("Enter second number:"))
c = int(input("enter third number:"))


def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(format(max3(a, b, c)))