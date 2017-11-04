y = input("Enter list 1:")
print(y.split())

x = input("Enter list 2:")
print(x.split())

for i in x.split():
    for j in y.split():
        if i is j:
            print(True)
        else:
            print(False)
