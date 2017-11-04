x = input("Please Enter a list of words:->")
print(x.split())

n = int(input("List all words shorter than:->"))


def filter(n, x):
    k = ''
    for i in x.split():
        if len(i) < n:
            k+=i
    return k

print("the following word(s) are shorter than {} is {}".format(n,filter(n,x)))