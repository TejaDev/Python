x = input("enter the first number:")
print("you entered:", x)

y = input("enter the second number:")
print("you entered:", y)

z = input("enter the third number:")
print("you entered:", z)


if((x>y) & (x>z)):
    print("The Maximum Value is:",x)
elif(y>z):
    print("The Maximum Value is:",y)
else:
    print("The Maximum Value is:",z)