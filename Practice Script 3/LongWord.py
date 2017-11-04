y = input("Enter list:")
print(y.split())

def maps(x):
    k = []
    for i in x.split():
        k.append(len(i))
    return (k)

print(maps(y))