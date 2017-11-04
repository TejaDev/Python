string = input("enter the String:")
print("you entered:", string)

def reverse(x):
    i=0
    for x in string:
        i += 1

    return string[-1::-1]

print(format(reverse(string)))