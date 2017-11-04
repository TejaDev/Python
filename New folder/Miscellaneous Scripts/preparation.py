def max(num):
    temp = num[0]
    for x in num:
        if x > temp:
            temp = x
    print(temp)

a = input("enter the numbers in the list: ")
b = a.split()
max(b)