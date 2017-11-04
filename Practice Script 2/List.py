x = input("Enter a value:")
print(x)

a = input("Enter list of numbers:")
print(a.split())


def is_member(x, a):
    i = 0
    while i < len(a.split()):
        if x == a.split()[i]:
            print(True)
        else:
            print(False)

        i += 1


format(is_member(x,a))