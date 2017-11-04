string = input("enter the String:")
print("you entered:", string)

i=0

for x in string:
    i += 1

print("the length of string is:", i)
print("the reversed dtring is ",string[-1::-1])
