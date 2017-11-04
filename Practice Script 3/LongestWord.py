y = input("Enter list:")
print(y.split())

n = int(input("Enter a number:"))


def filter_long_words(l, n):
    k = []
    for i in l.split():
        if len(i) > n:
            k.append(i)
    return k

print(filter_long_words(y,n))