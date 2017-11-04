x = input("Enter a list of words:->")
print(x.split())

def maps(x):
    k = []
    for i in x.split():
        k.append(len(i))
    return min(k)

print("The shortest word has {} charachters.".format(maps(x)))