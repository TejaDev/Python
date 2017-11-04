x = input("enter a list of number:->")

def min(a):
    z = 100
    for i in a.split():
        if int(i) < int(z):
            z = i
    return z
print("The Smallest number is {}".format(min(x)))