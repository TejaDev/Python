words = input("Please enter a list of words:->")


def Length(x):
    i = 0
    for x in words.split():
        i=i+1
    return i

print("The list of lengths of each word is: {}".format(Length(words)))