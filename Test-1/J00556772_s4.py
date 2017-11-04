x = input("Please Enter the first number:->")
y = input("Please Enter the second number:->")

def smallest(a,b):
    if (x < y):
        return x
    else:
        return y

print("The smallest number is {}".format(smallest(x,y)))