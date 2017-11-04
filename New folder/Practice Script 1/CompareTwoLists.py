y = input("Enter list 1:")
print(y.split())

x = input("Enter list 2:")
print(x.split())

if set(x) & set(y):
    print ("True")
else:
    print ("False")