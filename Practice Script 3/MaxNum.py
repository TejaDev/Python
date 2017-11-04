a = input("Enter the list of numbers:")
b = a.split()

def max_in_list(b):
    q = 0
    for i in range(len(b) - 1):
        if int(b[i]) > q and int(b[i]) > int(b[i + 1]):
            q = b[i]
        elif int(b[i + 1]) > q:
            q = int(b[i + 1])
    print(q)

max_in_list(b)


def max(num):
    temp = num[0]
    for x in num:
        if int(x)  > int(temp):
            temp = x
    print(temp)

max(b)
