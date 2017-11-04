y = input("Enter list:")
print(y.split())

x = input("Enter a value:")
print(x)

i = 0
while i < len(y.split()):
    if x == y.split()[i]:
        print(True)
    else:
        print(False)
    i += 1




