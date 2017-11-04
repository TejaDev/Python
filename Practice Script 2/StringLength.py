string = input("enter the String:")
print("you entered:", string)

def Length(x):
    i = 0
    for x in string:
        i=i+1
    return i

print(format(Length(string)))