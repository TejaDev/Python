y = input("Enter list 1:")
print(y.split())

x = input("Enter list 2:")
print(x.split())


def overlapping(y, x):
    for i in x.split():
        for j in y.split():
            if i is j:
                print(True)
            else:
                print(False)


overlapping(y,x)