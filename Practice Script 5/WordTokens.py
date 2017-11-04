import re

def avg_length(x):
    count = 0
    f = open(x)
    words = re.findall('\w+', f.read())
    print(words)
    for word in words:
        count += len(word)
        return (count/len(words))

print (avg_length('Token.txt'))